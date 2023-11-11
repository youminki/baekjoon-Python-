# 치킨 배달 15686
"""https://www.acmicpc.net/problem/15686"""

from itertools import combinations

N,M = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
house = [] # 일반 집
chicken = [] # 치킨 집
res = int(1e9)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i,j))
        elif arr[i][j] == 2:
            chicken.append((i,j))


for j in combinations(chicken, M):
    total = 0
    for i in house:
        tmp = int(1e9)
        for k in j:
            print("치킨집 위치", k)
            tmp = min(tmp, abs(k[0]-i[0])+abs(k[1]-i[1]))
            print("chicken",k[0],k[1])
            print("house", i[0],i[1])
            print("치킨집 ~ 집 거리 = ", min(tmp, abs(k[0]-i[0])+abs(k[1]-i[1])))
        total+=tmp
        print(total)
    res = min(res, total)
        
print(res)