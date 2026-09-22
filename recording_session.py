class RecordingSession:
    # A recording session belongs to one speaker and contains all the observations from that recording
    def __init__(self, speaker_profile, observations):
        self.speaker_profile = speaker_profile
        self.observations = observations