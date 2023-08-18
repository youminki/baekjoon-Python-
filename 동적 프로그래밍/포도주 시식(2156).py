# 포도주 시식(2156).py
""" https://www.acmicpc.net/problem/2156 """

import sys

input = sys.stdin.readline
n = int(input())
drink = [0] * 10001

for i in range(1, n + 1):
    drink[i] = int(input())
    
dp = [0] * 10001
dp[1] = drink[1]
dp[2] = drink[1] + drink[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + drink[i - 1] + drink[i], dp[i - 2] + drink[i], dp[i - 1])
print(dp[n])


"""#-------------------------------------
import sys

input = sys.stdin.readline
n = int(input()) # 음료의 개수를 입력 받습니다.
drink = [0] * 10001 # 각 음료의 양을 저장할 리스트를 생성합니다.

for i in range(1, n + 1): # 음료의 양을 입력 받아 리스트에 저장합니다.
    drink[i] = int(input())

dp = [0] * 10001 # 동적 프로그래밍을 위한 리스트를 생성합니다.
# 초기값을 설정합니다.
dp[1] = drink[1]
dp[2] = drink[1] + drink[2]

for i in range(3, n + 1): # 동적 프로그래밍을 통해 최대 음료 양을 계산합니다.
    dp[i] = max(dp[i - 3] + drink[i - 1] + drink[i], dp[i - 2] + drink[i], dp[i - 1]) # 현재 음료를 선택하는 경우, 바로 전 음료까지 선택한 경우, 전전 음료까지 선택한 경우의 최대 음료 양 중 가장 큰 값을 선택하여 dp 리스트에 저장합니다.

# 최대 음료 양을 출력합니다.
print(dp[n])
"""
