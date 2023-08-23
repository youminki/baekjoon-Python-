# 유기농 배추(1012).py
""" https://www.acmicpc.net/problem/1012 """

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

def BFS(x, y):
    queue = [(x, y)]
    graph[x][y] = True
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                continue
            if graph[nx][ny] == 1:
                #graph[nx][ny] == graph[x][y] + 1
                queue.append((nx, ny))
                graph[nx][ny] == 0
                
for _ in range(T):
    M, N, K = list(map(int, input().split()))
    graph = [[0] * (N) for _ in range(M)]
    count = 0
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
    for a in range(M):
        for b in range(N):
            if graph[a][b] == 1:
                BFS(a, b)
                count += 1
print(count)

# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# DFS를 이용한 풀이
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] == 1:
                graph[nx][ny] == 0
                DFS(nx, ny)
for _ in range(T):
    M, N, K = list(map(int, input().split()))
    graph = [[0] * (N) for _ in range(M)]
    count = 0
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
    for a in range(M):
        for b in range(N):
            if graph[a][b] == 1:
                DFS(a, b)
                count += 1
print(count)
                
"""for _ in range(N):
    graph.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = [[0, 0]]
while q:
    x, y = q.pop(0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
                count + 1
print(count)

"""