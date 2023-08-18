""" https://www.acmicpc.net/problem/12865 """
# 평범한 배낭(12865).py
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
add = [[0,0]]
dp = [[0] * (10001) for _ in range(101)]

for i in range(1, N + 1):
    W, V = map(int, input().split())
    add.append([W, V])
    
for i in range(1, N + 1):
    for j in range(1, K + 1):
        W = add[i][0] # 물품의 무게
        V = add[i][1] # 물품의 가치
        if W <= j:
            dp[i][j] = max(dp[i - 1][j], V + dp[i - 1][j - W])
        else:
            dp[i][j] = dp[i - 1][j]
            
print(dp[N][K])


#---------------------------------------
"""import sys

input = sys.stdin.readline
N, K = map(int, input().split())# 물품의 수 N과 가방의 용량 K 입력 받기
dp = [0] * (K + 1)# 가치의 합을 저장할 리스트 초기화

# 가치의 합을 저장할 리스트 초기화
for _ in range(N):
    W, V = map(int, input().split())# 물건의 무게 W와 가치 V 입력 받기
    # 현재 가방의 용량부터 물건의 무게까지 역순으로 반복
    for i in range(K, W - 1, -1):
        dp[i] = max(dp[i - W] + V, dp[i])# 이전에 구한 가치와 현재 물건의 가치를 비교하여 최댓값 저장
print(dp[K])# 가방의 용량 K에서 얻을 수 있는 최대 가치 출력


"""