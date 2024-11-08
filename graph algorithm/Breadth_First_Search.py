# breadth first search

from collections import deque

# making Adjacency list
N, M = [int(e) for e in input().split()]

Adj_list = [[] for e in range(N + 1)]
for m in range(M):
    A, B = [int(e) for e in input().split()]
    Adj_list[A].append(B)
    Adj_list[B].append(A)

# BFS
distance = [-1] * (N + 1)
distance[1] = 0
Q = deque()
Q.append(1)
while len(Q) >= 1:
    position = Q.popleft()
    for next in Adj_list[position]:
        if distance[next] == -1:
            distance[next] = distance[position] + 1
            Q.append(next)

for i in range(1, N + 1):
    print(distance[i])