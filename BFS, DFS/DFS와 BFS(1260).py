from collections import deque

N, M, V = list(map(int, input().split()))
graph = [[0] * (1001) for i in range(1001)]
visited_DFS = [0] * (N + 1)
visited_BFS = [0] * (N + 1)

for i in range(M):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = True

#구현
def DFS(V):
    visited_DFS[V] = True
    print(V,end=' ')
    for i in range(1, N + 1):
        if(visited_DFS[i] == 0 and graph[V][i] == 1):
            DFS(i)

def BFS(V):
    queue = deque([V]) # deque는 스택과 큐의 기능을 모두 가지고 있는 객체로, 양방향에서 삽입과 삭제가 일어날 수 있는 자료구조이다
    visited_BFS[V] = True
    while queue:
        V=queue.popleft()
        print(V, end = ' ')
        for i in range(1, N + 1):
            if(visited_BFS[i] == 0 and graph[V][i] == 1):
                queue.append(i)
                visited_BFS[i] = True

DFS(V)
print()
BFS(V)

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
        if(visited_DFS[i] == 0 and graph[V][i] == 1): # 정점 i를 방문하지 않았고, 현재 점정에서 i에 간선이 있을 경우
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
from collections import deque

# 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
N,M,V = map(eval,input().split())

# 연결 그래프 생성
graph = [[False] * (N + 1) for _ in range(N + 1)]

# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 입력으로 주어지는 간선은 양방향이다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다
for _ in range(M):
    a,b = map(eval, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (N + 1) #DFS 방문기록
visited2 = [False] * (N + 1) #BFS 방문기록

#방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문

# DFS 재귀
def DFS(V):
    visited1[V] = True  #해당 정점 V 방문처리
    print(V, end=' ')
    # 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
    for i in range(1, N + 1): #i=1,2,...,N
        if not visited1[i] and graph[V][i]: #만약 정점 i를 방문하지 않았고 정점 V와 연결되어 있다면
            DFS(i)  # 정점 i를 이용해서 DFS(i) 호출 ( 깊이 우선 탐색 )

# DFS 스택 LIFO
def DFS_stack(V):
    s = deque([V])  #시간 복잡도가 낮은 deque 사용
    while s:        # s이 빌때 까지
        V = s.pop() #deque 의 제일 뒤의 값 꺼낸다.
        if not visited1[V]:
            print(V, end=' ')
            visited1[V] = True  # 해당 정점 V 방문처리
        # 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
        for i in range(N,0,-1):    #i=N,N-1,...,1
            if not visited1[i] and graph[V][i]: #만약 정점 i를 방문하지 않았고 정점 V와 연결되어 있다면
                s.append(i)         #정점 i 추가
                #visited1[i] = True  #정점 i 방문 처리

# BFS 큐 FIFO
def BFS(V):
    q = deque([V]) #시간 복잡도가 낮은 deque 사용
    while q:            #q가 빌때까지
        V = q.popleft() #deque 의 첫번째 값 꺼낸다.
        if not visited2[V]:
            print(V, end=' ')
            visited2[V] = True  # 해당 정점 V 방문처리
        # 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
        for i in range(1, N + 1): #i=1,2,...,N
            if not visited2[i] and graph[V][i]: #만약 정점 i를 방문하지 않았고 정점 V와 연결되어 있다면
                q.append(i)     #정점 i 추가
DFS(V)
print()
BFS(V)"""


"""
deque를 사용하는 이유는?
list의 pop 보다 시간복잡도가 낮은 deque의 popleft 사용하기 위해서
4 5 1
1 2
1 3
1 4
2 4
3 4



1
|______
|  |  |
2  3__4
|_____|

"""
