# 치킨 배달 15686
"""https://www.acmicpc.net/problem/15686"""

from itertools import combinations

N,M = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
house = [] # 일반 집
chicken = [] # 치킨 집
res = int(1e9) # 결과값 초기화

# 집과 치킨 집의 좌표 저장
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i,j))
        elif arr[i][j] == 2:
            chicken.append((i,j))

# 조합을 이용하여 M개의 치킨 집을 선택하는 경우의 수 계산
for j in combinations(chicken, M):
    total = 0 # 선택된 치킨 집들까지의 거리의 합을 저장할 변수
    # 각 일반 집에 대해 최소 치킨 거리 계산
    for i in house:
        tmp = int(1e9)
        for k in j:
            #print("치킨집 위치", k)
            tmp = min(tmp, abs(k[0]-i[0])+abs(k[1]-i[1])) # 현재 집과 선택된 치킨 집 사이의 거리 계산
            #print("chicken",k[0],k[1])
            #print("house", i[0],i[1])
            #print("치킨집 ~ 집 거리 = ", min(tmp, abs(k[0]-i[0])+abs(k[1]-i[1])))
        total+=tmp # 현재 일반 집에 대한 최소 치킨 거리를 전체 거리에 더함
        #print(total)
    res = min(res, total)
        
print(res)