# N과 M(2) 15650
"""https://www.acmicpc.net/problem/15650"""


# 15650번
n,m = list(map(int,input().split()))
s = []
def dfs(start):
    if len(s) == m: # 길이가 m인 리스트가 되면 출력하고 종료
        print(' '.join(map(str, s)))
        return
    for i in range(start, n + 1): # 현재 숫자부터 n까지 반복
        if i not in s: # 선택한 숫자가 리스트에 없다면 추가하고 다음 숫자를 찾도록 재귀 호출
            s.append(i)
            #print(s)
            dfs(i + 1)
            s.pop()  # 백트래킹: 선택한 숫자를 다시 제거하여 다른 경우의 수를 탐색
            
dfs(1)




from itertools import *

a,b=map(int,input().split())
for i in combinations(range(1,a+1),b):
    print(*i)