import string


class Cluster:
    def __init__(self, name: string, subclusters: list, baseDistMtrixIndex: int, isSingle: bool):
        self.name = name
        self.subclusters = subclusters
        self.baseDistMtrixIndex = baseDistMtrixIndex
        self.isSingle = isSingle
