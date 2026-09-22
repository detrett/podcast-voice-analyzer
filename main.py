from data_generator import available_scenarios
from sample_data import create_recording_session
from analyzer import Analyzer
from report import print_report

def run_scenario(scenario):
    session = create_recording_session(
        scenario,
        seed=42
    )

    analyzer = Analyzer(session)
    result = analyzer.analyze()

    print("\nScenario:", scenario)
    print_report(result)


def main():
    print("Podcast Voice and Recording Analyzer")

    scenarios = available_scenarios()

    for scenario in scenarios:
        run_scenario(scenario)


if __name__ == "__main__":
    main()