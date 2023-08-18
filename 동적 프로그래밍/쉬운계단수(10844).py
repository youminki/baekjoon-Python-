"""N = int(input())

dp = [[0] * 10 for _ in range(N + 1)]

for i in range(1, 10):
    dp[1][i] = 1

#구현
for i in range(2, N+1):
    for j in range(1, 9):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000
    dp[i][9] = dp[i-1][8]
    dp[i][0] = dp[i-1][1]


print(sum(dp[N]) % 1000000000)

# 쉬운계단수(10844).py"""
""" https://www.acmicpc.net/problem/10844 """

import sys

input = sys.stdin.readline
N =int(input())
dp = [[0] * 10 for _ in range(101)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(1, 9):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])  # 오른쪽 + 왼쪽
    dp[i][9] = dp[i-1][8] # 왼쪽 대각선
    dp[i][0] = dp[i-1][1] # 오른쪽 대각선


print(sum(dp[N]) % 1000000000)