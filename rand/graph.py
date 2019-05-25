#Undirected, unweighted Graph
class Graph(object):

    def __init__(self, graph_dict=None):
        if graph_dict in [0,None]:
            graph_dict = {}
        if type(graph_dict) is int:
            if graph_dict < 0:
                raise ValueError("Number of nodes can't be negative")
            self.__graph_dict = {}
            for i in range(1,graph_dict+1):
                self.__graph_dict[str(i)] = []
        if type(graph_dict) is dict:
            self.__graph_dict = graph_dict
        if type(graph_dict) is Graph:
            self.__graph_dict = dict(graph_dict.__graph_dict)

    def vertices(self):
        if not self.__graph_dict:
            return []
        return list(self.__graph_dict.keys())

    def len_vertices(self):
        return len(self.vertices())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        #get edge as tuple
        vertex1, vertex2  = edge
        self.__graph_dict[vertex1].append(vertex2)
        self.__graph_dict[vertex2].append(vertex1)

    def remove_edge(self, edge):
        #get edge as tuple
        vertex1, vertex2  = edge
        self.__graph_dict[vertex1].remove(vertex2)
        self.__graph_dict[vertex2].remove(vertex1)


    def base(self):
        if len(self.vertices()) > 0:
            return self.vertices()[0]

    def next_Node(self, vertex):
        if not self.__graph_dict[vertex]:
            return []
        return self.__graph_dict[vertex][0]

    def all_Node(self, vertex):
        return self.__graph_dict[vertex]

    def degree(self, vertex):
        return len(self.__graph_dict[vertex])

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                edges.append((vertex, neighbour))
        return edges

    def is_connected(self):
        if self.len_vertices() < 2: return True
        visited = []
        for i in self.vertices():
            visited.append(False)
        visited[0] = True
        oStack = [self.vertices()[0]]
        while len(oStack) > 0:
            v = oStack.pop();
            nodes = self.all_Node(v)
            for i in nodes:
                if not visited[int(i)]:
                    visited[int(i)] = True
                    oStack.append(i)
        if False in visited:
            return False
        return True

    def search_iterativ(self):
        S = [self.base()]
        visited = []
        while S:
            u = S.pop()
            if u not in visited:
                visited.append(u)
                for v in reversed(self.all_Node(u)):
                    S.append(v)
        return visited

    def search_recursiv(self, u, visited=[]):
        # u = startnode
        visited.append(u)
        for v in self.all_Node(u):
            if v not in visited:
                self.search_recursiv(v)
        return visited

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += ("\nedges: ")
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

if __name__ == "__main__":

    # g = {   "0" : ["1","2"],
    #         "1" : ["0","3","4","5"],
    #         "2" : ["0","3"],
    #         "3" : ["1","2","4","5"],
    #         "4" : ["1","3","5","6"],
    #         "5" : ["1","3","4","6"],
    #         "6" : ["4","5"]
    #     }

    g = { "0" : ["1","2","3"],
          "1" : ["0","6"],
          "2" : ["0","3","5"],
          "3" : ["0","2","4"],
          "4" : ["3"],
          "5" : ["2"],
          "6" : ["1"]
        }

    graph = Graph(g)
    print(graph.search_iterativ())
    print(graph.search_recursiv(graph.base()))


