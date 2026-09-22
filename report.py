from utils import format_metric

# With this function we can turn the dictionary data from the analyzer into a readable report
def print_report(result):
    print("\n=== Podcast Recording Analysis ===")

    print("Speaker:", result["speaker_id"])
    print("Usable speech windows:",
          result["usable_speech_windows"])

    print("\nDelivery classification:",
          result["classification"])

    quality = result["quality"]

    print("Recording quality:", quality["label"])
    print("Quality explanation:", quality["reason"])

    print("\nAcoustic measurements")
    print("Average pitch:", format_metric(result["average_pitch"]))
    print("Average energy:", format_metric(result["average_energy"]))
    print("Average speech rate:",
          format_metric(result["average_speech_rate"]))
    print("Average pause ratio:",
          format_metric(result["average_pause_ratio"]))
    print("Average background noise:",
          format_metric(result["average_background_noise"]))
    print("Average signal quality:",
          format_metric(result["average_signal_quality"]))

    print("\nDifference from usual speaker profile")
    print("Pitch difference:", format_metric(result["pitch_difference"]))
    print("Energy difference:", format_metric(result["energy_difference"]))
    print("Speech rate difference:",
          format_metric(result["speech_rate_difference"]))
    print("Pause ratio difference:",
          format_metric(result["pause_ratio_difference"]))