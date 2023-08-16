# 2xn타일링2(11727).py
""" https://www.acmicpc.net/problem/11727 """

import sys

input = sys.stdin.readline
n = int(input())
dp = [0] * 1001
dp[0] = 1
dp[1] = 1
dp[2] = 3 # 이건 생략해도 되는데 이렇게 정의하면 시간이 더 줄어듬
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] * 2

print(dp[n] % 10007)