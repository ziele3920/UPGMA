from ete3 import Tree
import numpy as np
import UPGMA

dataMatrix = np.genfromtxt("cc.csv", delimiter=',')
s = dataMatrix.shape
distanceMartix = dataMatrix[1:dataMatrix.shape[0]-1, 1:dataMatrix.shape[1]-1]
UPGMA.calculateTree(distanceMartix)

t = Tree("((kotek, (upa, pumpa)), (a,b),(dupa, (kupa, kal)));")
t.show()

