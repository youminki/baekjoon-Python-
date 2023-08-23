import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(T):
    M, N, K = map(int,input().split())
    graph = [[0] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
        
def DFS(x, y):
    graph[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] == 1:
                DFS(nx,ny)
                
count = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            count += 1
            DFS(i,j)
print(count)

# --------------------------------------------------------------------------------
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

T=int(input())
for i in range(T):
    m,n,k = map(int,input().split())
    graph=[[0]*m for _ in range(n)]
    for j in range(k):
        x,y=map(int,input().split())
        graph[y][x] = 1

result=0
for j in range(n):
    for h in range(m):
        if dfs(j,h)==True:
            result += 1
print(result)