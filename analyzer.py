class Analyzer:
    # The analyzer requires a full recording session
    def __init__(self, session):
        self.session = session

    # Simple function that returns the number of observations in a session
    def count_observations(self):
        return len(self.session.observations)

    # Function to calculate the average pitch
    def average_pitch(self):
        pitches = []

        # Only adding observations where speech was detected
        for observation in self.session.observations:
            if observation.speech_present:
                pitches.append(observation.pitch)

        # Return nothing if no pitches were detected
        if not pitches:
            return None

        # Return the average pitch otherwise
        return sum(pitches) / len(pitches)

    # Calculates the average energy, counting only observations with speech detected
    def average_energy(self):
        energies = []

        for observation in self.session.observations:
            if observation.speech_present:
                energies.append(observation.energy)

        if not energies:
            return None

        return sum(energies) / len(energies)

    # Calculates the average speech rate, counting only observations with speech detected
    def average_speech_rate(self):
        speech_rates = []

        for observation in self.session.observations:
            if observation.speech_present:
                speech_rates.append(observation.speech_rate)

        if not speech_rates:
            return None

        return sum(speech_rates) / len(speech_rates)

    
