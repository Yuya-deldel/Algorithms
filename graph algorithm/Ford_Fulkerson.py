# Maximum flow // Ford Fulkerson method

INF = 10 ** 10

class Maximum_Flow_Graph:
    def __init__(self, to, capacity, reverse):
        self.to = to
        self.capacity = capacity
        self.reverse = reverse

# depth first search
def DFS_flow(position, goal, flow, Graph, Used):
    if position == goal:
        return flow
    
    Used[position] = True
    for edge in Graph[position]:
        if (edge.capacity > 0) and (not Used[edge.to]):
            F = DFS_flow(edge.to, goal, min(flow, edge.capacity), Graph, Used)
            if F >= 1:
                edge.capacity -= F
                Graph[edge.to][edge.reverse].capacity += F
                return F
    
    return 0

def maximumFlow(N, vertex_x, vertex_y, edges):
    Graph = [ list() for i in range(N+1) ]
    for a, b, c in edges:
        Graph[a].append(Maximum_Flow_Graph(b, c, len(Graph[b])))
        Graph[b].append(Maximum_Flow_Graph(a, 0, len(Graph[a]) - 1))
    
    total_flow = 0
    while True:
        Used = [False] * (N+1)
        flow = DFS_flow(vertex_x, vertex_y, INF, Graph, Used)
        if flow > 0:
            total_flow += flow
        else:
            break
    
    return total_flow
