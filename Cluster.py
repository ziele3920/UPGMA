import string


class Cluster:
    def __init__(self, name: string, subclusters):
        self.name = name
        self.subclusters = subclusters
