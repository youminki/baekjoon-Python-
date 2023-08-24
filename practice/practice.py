N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 0

def DFS(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
            if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                if nx == N - 1 and ny == M - 1:
                    return
                DFS(nx, ny)
    return
DFS(0, 0)
print(visited[N - 1][M - 1])
#---------------------------------------
#BFS
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 0

def BFS(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return
BFS(0, 0)
print(visited[N - 1][M - 1])