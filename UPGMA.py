import numpy as np

import Cluster
import Matrix
import MergedPair


def calculateTree(matrix: Matrix):
    currentMatrix = matrix
    baseDistMatrix = matrix.distanceMatrix
    matrixList = list([matrix])
    mergingList = list()
    while currentMatrix.distanceMatrix.shape[0] > 2:
        currentMatrix = calculateNewMatrix(baseDistMatrix, currentMatrix, mergingList)
        matrixList.append(currentMatrix)
    return mergingList

def calculateDistance(baseDistMatrix, fcluster: Cluster, scluster: Cluster):
    sum = 0
    counter = 0
    for index in fcluster.baseDistMtrixIndexes:
        for index2 in scluster.baseDistMtrixIndexes:
            sum += baseDistMatrix[index, index2]
            counter += 1
    return sum/counter

def calculateNewMatrix(baseDistMatrix, matrix: Matrix, mergingList):
    minIndex = matrix.getMinIndex()
    firstMergingCluster = matrix.clusters[minIndex[0]]
    secondMergingCluster = matrix.clusters[minIndex[1]]
    newIndexes = list(firstMergingCluster.baseDistMtrixIndexes)
    newIndexes = newIndexes + list(secondMergingCluster.baseDistMtrixIndexes)
    newCluster = Cluster.Cluster(firstMergingCluster.name + " " + secondMergingCluster.name, list([firstMergingCluster, secondMergingCluster]), newIndexes, False)
    mergingList.append(MergedPair.MergedPair(firstMergingCluster, secondMergingCluster, baseDistMatrix[minIndex[0], minIndex[1]]))
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
        newDistanceColumn[ii] = calculateDistance(baseDistMatrix, newClusters[ii], newCluster)

    newDistanceMatrix = np.append(newDistanceColumn, newDistanceMatrix, axis=1)
    newDistanceRow = np.insert(newDistanceColumn, 0, 0)
    newDistanceMatrix = np.insert(newDistanceMatrix, 0, newDistanceRow, axis=0)
    newClusters.insert(0, newCluster)
    return Matrix.Matrix(newClusters, newDistanceMatrix)
