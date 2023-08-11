# 계단 오르기(2579).py
"""https://www.acmicpc.net/problem/2579"""

import sys

input = sys.stdin.readline
n = int(input())

stairs = [0] * 301
for i in range(1, n + 1):
    stairs[i] = int(input())

dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n])










"""#-------------------------------------------
#주석 o

import sys

input = sys.stdin.readline
n = int(input())

stairs = [0] * 301 # 계단의 숫자를 초기화 합니다. 1층은 1번째(not 0번째) 인덱스에 저장합니다. 최댓값이 조건에 300이라고 명시되어있음므로 n+1을해준다.(만약 최댓값이 명시되지 않은경우, n+1을 해주면 됨.)
for i in range(1, n + 1): # 각 계단의 점수를 입력받습니다.
    stairs[i] = int(input())

dp = [0] * 301 # dp 배열을 초기화합니다.위 stair과 마찬가지로 n+1만큼 곱해줍니다.
dp[1] = stairs[1] # 첫번째 계단은 값을 그대로 가져값니다.
dp[2] = stairs[1] + stairs[2] # 두번째 계단 = 첫번째 계단 + 두번째 계단
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3]) # 계단3  = 계단1 + 계단2 or 계단2 + 계단3 두가지중 max()함수를 사용하여 최댓값을 가져옵니다.

for i in range(4, n + 1): # 1 ~ 3계단은 이미 위에서 계산했기때문에 4번째 계단부터 계산하면된다.
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i]) # i-3까지의 계단 점수 최댓값과 i-1, i 계단의 합 or i-2까지의 계단 점수 최댓값과 i 계단의 합 중 max()함수를 사용해여 최댓값을 가져옵니다.
                                                                                # 즉 진전 칸에서 올라온 경우의 최댓값 or 전전칸에서 올라온 최댓값중 max값을 구하는 것이다.
print(dp[n])


#-------------------------------------------
#참고자료 : https://v3.leedo.me/devs/64"""