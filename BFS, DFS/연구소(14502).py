# 연구소 14502
"""https://www.acmicpc.net/problem/14502"""
from collections import deque

n,m = map(int,input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
graph = [list(map(int, input().split())) for _ in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            count += 1 #처음0의개수
res = 0

# dfs함수안에서 퍼지는 바이러스의 수를 구할 bfs함수
def bfs():
    visited = [[0] * m for _ in range(n)]
    global res
    # print(graph)
    result = 0
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                visited[i][j] = 1
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <=ny < m and visited[nx][ny]==0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    # graph[nx][ny] = 2
                    result += 1
                    q.append((nx,ny))
    # for i in range(n):
    #     for j in range(m):
    #         if graph[i][j] == 0:
    #             result += 1
    # dfs함수안에서는 안전영역 max 값( 2의 개수 최솟값)을 갱신해야한다.
    res = max(res,count-result)

# 조건에 벽의 개수 = 3개라 했음.
def wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(count+1)
                graph[i][j] = 0
wall(0)
print(res-3)

