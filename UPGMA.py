import numpy as np

import Cluster
import Matrix


def calculateTree(matrix: Matrix):
    minIndex = matrix.getMinIndex()
    firstMergingCluster = matrix.clusters[minIndex[0]]
    secondMergingCluster = matrix.clusters[minIndex[1]]
    newCluster = Cluster.Cluster(firstMergingCluster.name + secondMergingCluster.name, list([firstMergingCluster, secondMergingCluster]), None)
    newDistanceMatrix = matrix.distanceMatrix.copy()
    newClusters = list(matrix.clusters)
    newDistanceMatrix = np.delete(newDistanceMatrix, minIndex[0], 0)
    newDistanceMatrix = np.delete(newDistanceMatrix, minIndex[0], 1)
    newDistanceMatrix = np.delete(newDistanceMatrix, minIndex[1], 0)
    newDistanceMatrix = np.delete(newDistanceMatrix, minIndex[1], 1)
    newClusters.pop(minIndex[0])
    newClusters.pop(minIndex[1])
    newDistanceColumn = np.zeros([len(newClusters), 1])

    for ii in range(0, len(newClusters)):
        