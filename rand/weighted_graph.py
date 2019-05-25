import numpy as np
import math

class Weighted_Graph(object):

    class Edge(object):

        def __init__(self, nodes, weight):
            self.node1 = nodes[0]
            self.node2 = nodes[1]
            self.weight = weight

        def setWeight(self, w):
            self.weight = w

        def from_(self):
            return node1

        def to_(self):
            return node2

        def __str__(self):
            return "(({},{}) {})".format(self.node1, self.node2, self.weight)

    def __init__(self, V):
        self.adjMat = np.full((V,V), math.inf)

    def __str__(self):
        return str(self.adjMat)

graph = Weighted_Graph(10)
print(graph)

