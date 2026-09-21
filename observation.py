class Observation:
    # Observation class, each observation represents one timestamp of the recording
    def __init__(self, timestamp, speech_present, pitch, energy,
                 speech_rate, pause_ratio, background_noise, signal_quality):
        self.timestamp = timestamp
        self.speech_present = speech_present
        self.pitch = pitch
        self.energy = energy
        self.speech_rate = speech_rate
        self.pause_ratio = pause_ratio
        self.background_noise = background_noise
        self.signal_quality = signal_quality