import numpy as np
import sys


class Matrix:
    def __init__(self, clusters, distanceMatrix: np.ndarray):
        self.clusters = clusters
        self.distanceMatrix = distanceMatrix

    def getMinIndex(self):
        minValue = sys.float_info.max
        minIndex = np.array([0,0])
        matrixSize = self.distanceMatrix.shape[0]
        for x in range(0, matrixSize-1):
            for y in range(x+1, matrixSize):
                if self.distanceMatrix[y, x] < minValue:
                    minValue = self.distanceMatrix[y, x]
                    minIndex = np.array([y, x])
        return minIndex