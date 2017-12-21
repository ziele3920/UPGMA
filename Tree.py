import string

from ete3 import Tree

import Cluster


class TreeNode:
    def __init__(self, cluster1: Cluster, cluster2: Cluster, node1, node2):
        self.cluster1 = cluster1
        self.cluster2 = cluster2
        self.left = node1
        self.right = node2
        self.leaf = False
        if node1 is None:
            self.leaf = True


class GraphicalNode:
    def __init__(self, names: list, graphicalString: string):
        self.names = names
        self.graphicalString = graphicalString
        self.singleClustersNo = len(names)

    def equalNode(self, names):
        counter = len(names)
        for name in names:
            for nName in self.names:
                if name == nName:
                    counter = counter - 1
                    continue
        if counter is 0:
            return True
        return False


class GraphicalTree:
    def __init__(self, mergingList):
        self.nodes = list()

        for pair in mergingList:
            print(pair.cluster1.name + " & " + pair.cluster2.name)
            self.addNode(pair.cluster1, pair.cluster2)

    def showTree(self):
        t = Tree(self.nodes[0].graphicalString + ";")
        t.show()

    def addNode(self, cluster1: Cluster, cluster2: Cluster):
        cluster1String = ""
        cluster2String = ""

        if cluster1.isSingle:
            cluster1String = cluster1.name
        else:
            node = self.getNode(cluster1)
            cluster1String = node.graphicalString

        if cluster2.isSingle:
            cluster2String = cluster2.name
        else:
            node = self.getNode(cluster2)
            cluster2String = node.graphicalString

        mergedString = "(" + cluster1String + "," + cluster2String + ")"
        nodeNames = cluster1.name.split() + cluster2.name.split()
        self.nodes.append(GraphicalNode(nodeNames, mergedString))



    def getNode(self, cluster):
        names = cluster.name.split()
        node: GraphicalNode = None
        for i in range(0, len(self.nodes)):
            if len(names) != self.nodes[i].singleClustersNo:
                continue
            if self.nodes[i].equalNode(names):
                node = self.nodes.pop(i)
                break
        return node
