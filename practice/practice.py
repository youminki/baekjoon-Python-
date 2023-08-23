import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(101)]
visited = [0] * (N + 1)

for  _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
def DFS(M):
    visited[M] = True
    for i in graph[M]:
        if visited[i] == 0:
            DFS(i)

DFS(1)
print(sum(visited) - 1)



