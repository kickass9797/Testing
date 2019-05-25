from graph import Graph

g = {   "0" : ["1","2"],
        "1" : ["0","3","4","5"],
        "2" : ["0","3"],
        "3" : ["1","2","4","5"],
        "4" : ["1","3","5","6"],
        "5" : ["1","3","4","6"],
        "6" : ["4","5"]
    }

# g = {   "0" : ["1","3"],
#         "1" : ["0","2"],
#         "2" : ["1","3"],
#         "3" : ["0","2"]
#     }

graph = Graph(g)
def euler_round(graph):
    if not graph.is_connected(): return []
    for i in graph.vertices():
        if graph.degree(i) % 2 == 1:
            return []
    oTour = []
    hStack = []
    hGraph = Graph(graph)
    v = hGraph.base()
    hStack.append(v)
    while len(hStack) > 0:
        v = hStack.pop()
        oTour.append(v)
        while hGraph.degree(v) > 0:
            hStack.append(v)
            w = hGraph.next_Node(v)
            hGraph.remove_edge((v,w))
            v = w
    return(oTour)

print(euler_round(graph))

