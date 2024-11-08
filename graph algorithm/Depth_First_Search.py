# Depth First Search ~ O(Vertex + Path)

import sys
sys.setrecursionlimit(130000)

def DFS(position, Adjacency_list, visited):
    visited[position] = True
    for i in Adjacency_list[position]:
        if visited[i] == False:
            DFS(i, Adjacency_list, visited)

###########################################
# making Adjacency list
N, M = [int(e) for e in input().split()]

Adj_list = [[] for e in range(N + 1)]
for m in range(M):
    A, B = [int(e) for e in input().split()]
    Adj_list[A].append(B)
    Adj_list[B].append(A)


# DFS
visited = [False] * (N + 1)
DFS(1, Adj_list, visited)

# connected or not
answer = True
for i in range(1, N + 1):
    if not visited[i]:
        answer = False


if answer:
    print("The graph is connected.")
else:
    print("The graph is not connected.")