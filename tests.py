import unittest

from analyzer import Analyzer
from observation import Observation
from sample_data import create_recording_session


class TestObservation(unittest.TestCase):
    # This test checks that an impossible energy value is rejected
    def test_invalid_energy_is_rejected(self):
        with self.assertRaises(ValueError):
            Observation(
                timestamp=0,
                speech_present=True,
                pitch=170,
                energy=1.5,
                speech_rate=110,
                pause_ratio=0.2,
                background_noise=0.1,
                signal_quality=0.9
            )
    # An observation without speech cant have meaningful speech measurements, so those values are allowed to be None
    def test_missing_speech_values_are_allowed_without_speech(self):
        observation = Observation(
            timestamp=0,
            speech_present=False,
            pitch=None,
            energy=None,
            speech_rate=None,
            pause_ratio=None,
            background_noise=0.3,
            signal_quality=0.4
        )

        self.assertFalse(observation.speech_present)


class TestAnalyzer(unittest.TestCase):
    # The generated consistent scenario should stay close enough to the speaker's usual profile to be classified as consistent
    def test_consistent_scenario(self):
        session = create_recording_session("consistent", seed=42)
        analyzer = Analyzer(session)

        self.assertEqual(
            analyzer.classify_delivery(),
            "consistent"
        )
    # The energetic scenario increases the speaker's energy and speech rate, so it should be detected as energetic
    def test_energetic_scenario(self):
        session = create_recording_session("energetic", seed=42)
        analyzer = Analyzer(session)

        self.assertEqual(
            analyzer.classify_delivery(),
            "energetic"
        )
    # The deliberate scenario has a lower speech rate and higher pause ratio than the speaker's usual profile
    def test_deliberate_scenario(self):
        session = create_recording_session("deliberate", seed=42)
        analyzer = Analyzer(session)

        self.assertEqual(
            analyzer.classify_delivery(),
            "deliberate"
        )
    # High background noise should be identified separately
    def test_noise_scenario(self):
        session = create_recording_session("noise_affected", seed=42)
        analyzer = Analyzer(session)

        self.assertEqual(
            analyzer.classify_delivery(),
            "noise affected"
        )
    # Most of the windows in this scenario do not contain speech so the analyzer should classify it accordingly
    def test_insufficient_data_scenario(self):
        session = create_recording_session("insufficient_data", seed=42)
        analyzer = Analyzer(session)

        self.assertEqual(
            analyzer.classify_delivery(),
            "insufficient data"
        )
    # The analysis must return a structured dictionary to be used by other parts of the application
    def test_analysis_returns_dictionary(self):
        session = create_recording_session("consistent", seed=42)
        analyzer = Analyzer(session)

        result = analyzer.analyze()

        self.assertIsInstance(result, dict)
        self.assertIn("classification", result)
        self.assertIn("quality", result)
    # Values within the tolerance should return True, while values outside the tolerance should return False.
    def test_static_tolerance_method(self):
        self.assertTrue(
            Analyzer.is_within_tolerance(8, 10)
        )

        self.assertFalse(
            Analyzer.is_within_tolerance(15, 10)
        )


if __name__ == "__main__":
    unittest.main()