import string


class Cluster:
    def __init__(self, name: string, subclusters: list, baseDistMtrixIndexes: list, isSingle: bool):
        self.name = name
        self.subclusters = subclusters
        self.baseDistMtrixIndexes = baseDistMtrixIndexes
        self.isSingle = isSingle


def generateSingleClustersList(names):
    clusters = list()
    for x in range(0, len(names)):
        clusters.append(Cluster(names[x], None, list([x]), True))
    return clusters
