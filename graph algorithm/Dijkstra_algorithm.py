# Dijkstra's algorithm

import heapq

INF = 10 ** 10

# making weighted graph

N, M = [int(e) for e in input().split()]
Adj_list = [[] for e in range(N + 1)]
for m in range(M):
    A, B, W = [int(e) for e in input().split()]
    Adj_list[A].append((B, W))
    Adj_list[B].append((A, W))

# Dijkstra's algorithm // (distance, vertex) in heapqueue
def Dijkstra(Adj_list, start):
    N = len(Adj_list) - 1
    determined = [False] * (N + 1)
    distance = [INF] * (N + 1)
    distance[start] = 0
    Q = []
    heapq.heappush(Q, (0, 1))
    while len(Q) >= 1:
        position = heapq.heappop(Q)[1]      # position = vertex which has minimum distance
        if determined[position] == True:
            continue

        determined[position] = True
        for tupl in Adj_list[position]:                                 # tupl = (vertex, weight)
            if (distance[tupl[0]] > distance[position] + tupl[1]):
                distance[tupl[0]] = distance[position] + tupl[1]
                heapq.heappush(Q, (distance[tupl[0]], tupl[0]))

    return distance


# output
# distance
distance = Dijkstra(Adj_list, 1)
for i in range(1, N + 1):
    if distance[i] != INF:
        print(distance[i])
    else:
        print(-1)

# path from 1 to N
Vertex = [N]
position = N
while position != 1:
    Min = INF
    for tupl in Adj_list[position]:
        D = distance[tupl[0]] + tupl[1]
        if Min >= D:
            V = tupl[0]
            Min = D 
    
    position = V
    Vertex.append(V)

L = len(Vertex)
for j in range(L-1, -1, -1):
    print(Vertex[j], end=" ")