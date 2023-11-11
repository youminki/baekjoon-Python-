# N과 M(2) 15650
"""https://www.acmicpc.net/problem/15650"""


# 15650번
n,m = list(map(int,input().split()))
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)





# from itertools import combinations
# n, m = map(int, input().split())
# for i in combinations([i for i in range(1, n + 1)], m):
#     print(*i)
