# 유기농 배추(1012).py
""" https://www.acmicpc.net/problem/1012 """
from collections import deque


def bfs(x, y):
    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if graph[y][x] == 1:
        queue.append((x, y))
        visited[y][x] = True
        count = 1
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0 <= nx < M and 0 <= ny < N:
                    if visited[ny][nx] == 0 and graph[ny][nx] == 1:
                        visited[ny][nx] = True
                        queue.append((nx,ny))
                        count += 1
    return count

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * (N) for i in range(M)]
    visited = [[False]*M for i in range(N)]
    list = []
    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1
    for i in range(M):
        for j in range(N):
            if graph[j][i] == 1 and visited[j][i] == False:
                list.append(bfs(i, j))
    print(len(list))

#---------------------------------------------
# DFS
import sys

sys.setrecursionlimit(10000)

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                DFS(nx,ny)

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * (N) for i in range(M)]
    for _ in range(K):
        x,y = map(int, input().split())
        graph[x][y] = 1

    count = 0
    visited = [[0] * N for i in range(M)]

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1 and visited[i][j] == 0:
                DFS(i,j)
                count+=1
                
    print(count)