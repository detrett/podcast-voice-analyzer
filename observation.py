class Observation:
    # Observation class, each observation represents one timestamp of the recording
    def __init__(self, timestamp, speech_present, pitch, energy,
                 speech_rate, pause_ratio, background_noise, signal_quality):

        # Validation of values
        if pitch < 0:
            raise ValueError("Pitch cannot be a negative value")

        if energy < 0 or energy > 1:
            raise ValueError("Energy value must be between 0 and 1")

        if speech_rate < 0:
            raise ValueError("Speech rate cannot be a negative value")

        if pause_ratio < 0 or pause_ratio > 1:
            raise ValueError("Pause ratio must be between 0 and 1")

        if background_noise < 0 or background_noise > 1:
            raise ValueError("Background noise must be between 0 and 1")

        if signal_quality < 0 or signal_quality > 1:
            raise ValueError("Signal quality must be between 0 and 1")

        self.timestamp = timestamp
        self.speech_present = speech_present
        self.pitch = pitch
        self.energy = energy
        self.speech_rate = speech_rate
        self.pause_ratio = pause_ratio
        self.background_noise = background_noise
        self.signal_quality = signal_quality