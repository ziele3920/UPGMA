import numpy as np
import sys

def calculateTree(distanceMatrix):
    for x in range(0, distanceMatrix.shape[0]):
        distanceMatrix[x, x] = sys.float_info.max
    while distanceMatrix.size > 2:
        minIndex = np.unravel_index(distanceMatrix.argmin(), distanceMatrix.shape)


