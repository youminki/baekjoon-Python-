from collections import deque

N, M = map(int, input().split())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = [[0, 0]]
for i in range(N):
    graph.append(list(map(int, input())))
    
while q:
    x, y = q.pop(0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
print(graph[N - 1][M - 1])