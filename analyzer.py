class Analyzer:
    # The analyzer requires a full recording session
    def __init__(self, session):
        self.session = session

    # Simple function that returns the number of observations in a session
    def count_observations(self):
        return len(self.session.observations)

    