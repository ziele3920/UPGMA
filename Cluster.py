import string


class Cluster:
    def __init__(self, name: string, subclusters: list, baseDistMtrixIndexes: list, isSingle: bool):
        self.name = name
        self.subclusters = subclusters
        self.baseDistMtrixIndexes = baseDistMtrixIndexes
        self.isSingle = isSingle
