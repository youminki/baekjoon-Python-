# 11724(연결 요소의 개수).py
""" https://www.acmicpc.net/problem/11724 """
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(1001)]
visited = [False] * (N + 1)
count = 0
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

for i in range(1, N + 1):
    if visited[i] == False:
        BFS(i)
        count += 1
print(count)


"""#--------------------------------
# DFS로 푸는 방법

import sys

sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(1001)]
visited = [False] * (N + 1)
count = 0
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def DFS(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            DFS(i)

for i in range(1, N + 1):
    if visited[i] == False:
        DFS(i)
        count += 1
print(count)

#--------------------------------
"""