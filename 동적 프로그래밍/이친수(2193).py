# 이친수(2193).py
""" https://www.acmicpc.net/problem/2193 """

import sys

input = sys.stdin.readline
n = int(input())

dp = [0, 1, 1]

for i in range(3, n + 1):
    result = dp[i - 1] + dp[i - 2]
    dp.append(result)
print(dp[n])

"""#--------------------------------
import sys

input = sys.stdin.readline
n = int(input())

dp = [0, 1, 1] # dp[0] = 0, dp[1] = 1 -> 1 dp[2] = 10 -> 1

for i in range(3, n + 1):
    result = dp[i - 1] + dp[i - 2]
    dp.append(result)
print(dp[n])"""
