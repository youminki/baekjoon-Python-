# 연구소 14502
"""https://www.acmicpc.net/problem/14502"""
from collections import deque

# 입력:
# n -> 행의 수
# m -> 열의 수
n, m = map(int, input().split())

# 방향 이동 (상, 하, 우, 좌)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = [list(map(int, input().split())) for _ in range(n)] # 입력: 격자를 나타내는 2D 배열
count = 0 # 초기 '0'의 개수를 추적하는 변수 초기화

for i in range(n): # 격자에서 초기 '0'의 개수를 세기
    for j in range(m):
        if graph[i][j] == 0:
            count += 1
res = 0# 결과를 0으로 초기화

def bfs(): # 바이러스 전파를 찾기 위한 너비 우선 탐색(BFS)을 수행하는 함수
    visited = [[0] * m for _ in range(n)] # 방문한 노드를 추적하는 2D 배열 생성
    global res # 결과를 업데이트하기 위해 전역 변수 'res' 사용
    result = 0 # 이 BFS의 결과를 초기화
    q = deque() # BFS에 사용할 q 생성
    for i in range(n): # 초기 바이러스 위치로 큐 초기화
        for j in range(m):
            if graph[i][j] == 2:
                visited[i][j] = 1
                q.append((i, j))
    while q: # BFS 수행
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    result += 1
                    q.append((nx, ny))
    res = max(res, count - result) # 초기 '0'들을 고려하여 최대 결과를 업데이트

def wall(count): # 바이러스를 억제하기 위해 벽을 세우는 함수
    if count == 3: # 세 개의 벽이 세워졌을 때 BFS 수행(문제 조건 3개의 벽)
        bfs()
        return
    for i in range(n): # 각 가능한 위치에 벽을 세우기 시도
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1  # 벽 세우기
                wall(count + 1)  # 다음 벽을 위해 재귀 호출
                graph[i][j] = 0  # 백트래킹: 벽 제거
                
wall(0) # 벽이 없이 시작
print(res - 3) # 초기 '0'들과 세 개의 벽을 고려하여 최대 결과 출력
