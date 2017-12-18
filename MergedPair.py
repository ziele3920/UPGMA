import Cluster


class MergedPair:
    def __init__(self, cluster1: Cluster, cluster2: Cluster, dist: float):
        self.cluster1 = cluster1
        self.cluster2 = cluster2
        self.distance = dist