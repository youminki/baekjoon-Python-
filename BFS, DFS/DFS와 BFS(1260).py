# DFS와 BFS(1260).py
""" https://www.acmicpc.net/problem/1260 """
from collections import deque

N, M, V = list(map(int, input().split()))
graph = [[0] * (1001) for i in range(1001)]
visited_DFS = [False] * (N + 1)
visited_BFS = [False] * (N + 1)

for i in range(M):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = True

#구현
def DFS(V):
    visited_DFS[V] = True
    print(V,end = " ")
    for i in range(1, N + 1):
        if(visited_DFS[i] == False and graph[V][i] == True):
            DFS(i)

def BFS(V):
    queue = deque([V]) # deque는 스택과 큐의 기능을 모두 가지고 있는 객체로, 양방향에서 삽입과 삭제가 일어날 수 있는 자료구조이다
    visited_BFS[V] = True
    while queue:
        V = queue.popleft()
        print(V, end = " ")
        for i in range(1, N + 1):
            if(visited_BFS[i] == False and graph[V][i] == True):
                queue.append(i)
                visited_BFS[i] = True

DFS(V)
print()
BFS(V)
"""
# ---------------------------
# 주석 버전
from collections import deque

N, M, V = list(map(int, input().split())) # N = 정점의 개수, M = 간선의 개수, V = 탐색을 시작할 정점의 번호
graph = [[0] * (1001) for i in range(1001)] # 모든 요소가 0으로 초기화된 인접 행렬(그래프)을 생성
visited_DFS = [0] * (N + 1) # 정점을 추적하기 위한 배열을 생성
visited_BFS = [0] * (N + 1) # 정점을 추적하기 위한 배열을 생성

for i in range(M): # 간선의 개수만큼 반복
    a,b = map(int, input().split()) # 간선의 정보를 입력받고 인접 행렬을 채웁니다.
    graph[a][b] = graph[b][a] = True  # 인접 행렬에서 해당 위치에 True를 설정하여 간선을 나타냅니다.

# DFS 버전(깊이 우선 탐색)
def DFS(V):
    visited_DFS[V] = True # 현재 정점을 방분했다고 True로 표시
    print(V,end=' ') # 현재 정점을 출력
    for i in range(1, N + 1): # 모든 인접 정점 탐색
        if(visited_DFS[i] == 0 and graph[V][i] == 1): # 정점 i를 방문하지 않았고, 현재 정점에서 i에 간선이 있을 경우
            DFS(i) # i 정점으로 DFS를 호출합니다(재귀)
# BFS 버전 (선형 우선 탐색)
def BFS(V):
    queue = deque([V]) # deque는 스택과 큐의 기능을 모두 가지고 있는 객체로, 양방향에서 삽입과 삭제가 일어날 수 있는 자료구조이다
    visited_BFS[V] = True # 현재 정점을 방분했다고 True로 표시
    while queue: # q가 빌 때까지 반복
        V = queue.popleft() # 큐에서 정점을 추출
        print(V, end = ' ') # 추출한 정점 출력
        for i in range(1, N + 1): # 모든 인접 정점 탐색
            if(visited_BFS[i] == 0 and graph[V][i] == 1): # 정점 i를 방문하지 않았고, 현재 점정에서 i에 간선이 있을 경우
                queue.append(i) # 큐에 i를 삽입
                visited_BFS[i] = True # 방문했다고 True로 표시

DFS(V)
print() # 줄바꿈
BFS(V)


# ---------------------------
"""