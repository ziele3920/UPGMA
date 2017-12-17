import numpy as np
import sys

import Matrix


def calculateTree(matrix: Matrix):
    for x in range(0, matrix.distanceMatrix.shape[0]):
        matrix.distanceMatrix[x, x] = sys.float_info.max
    while matrix.distanceMatrix.size > 2:
        minIndex = np.unravel_index(matrix.distanceMatrix.argmin(), matrix.distanceMatrix.shape)


