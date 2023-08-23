from collections import deque

N, M, V = list(map(int, input().split()))
graph = [[0] * (1001) for _ in range(1001)]
visited_DFS = [False] * (N + 1)
visited_BFS = [False] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True
    
def DFS(V):
    visited_DFS[V] = True
    print(V, end = " ")
    for i in range(1, N + 1):
        if (visited_DFS[i] == False and graph[V][i] == True):
            DFS(i)
def BFS(V):
    queue = deque([V])
    visited_BFS[V] = True
    while queue:
        V = queue.popleft()
        print(V, end = " ")
        for i in range(1, N + 1):
            if (visited_BFS[i] == False and graph[V][i] == True):
                queue.append(i)
                visited_BFS[i] = True
DFS(V)
print()
BFS(V)
