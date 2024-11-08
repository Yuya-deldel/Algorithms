# Bellman_Ford's algorithm

INF = 10 ** 10

##################################################

N, M = [int(e) for e in input().split()]
Adj_list = [[] for e in range(N + 1)]
for m in range(M):
    A, B, W = [int(e) for e in input().split()]
    Adj_list[A].append((B, W))
    Adj_list[B].append((A, W))


def Bellman_Ford(Adj_list, start):
    N = len(Adj_list) - 1
    distance = [INF] * (N + 1)
    distance[start] = 0
    for i in range(1, N):
        for position in range(1, N):
            for tupl in Adj_list[position]:
                distance[tupl[0]] = min(distance[tupl[0]], distance[position] + tupl[1])

    for position in range(1, N):
        for tupl in Adj_list[position]:
            if distance[tupl[0]] > distance[position] + tupl[1]:
                raise ValueError('Negative cycle detected')

    return distance

#######################################################

N, M = [int(e) for e in input().split()]
A = [0] * M
B = [0] * M
W = [0] * M
for m in range(M):
    A[m], B[m], W[m] = [int(e) for e in input().split()]

def Bellman_Ford2(A, B, W, N, start):
    distance = [INF] * (N + 1)
    distance[start] = 0
    for i in range(1, N):
        for j in range(M):
            distance[B[j]] = min(distance[B[j]], distance[A[j]] + W[j])
            distance[A[j]] = min(distance[A[j]], distance[B[j]] + W[j])
    
    for j in range(M):
        if distance[B[j]] > distance[A[j]] + W[j]:
            raise ValueError('Negative cycle detected')

    return distance    

#########################################################

distance = Bellman_Ford2(A, B, W, N, 1)

# output
# distance
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