# 다리놓기(1010).py
""" https://www.acmicpc.net/problem/1010 """

import sys

input = sys.stdin.readline
T = int(input())
dp = [[0] * 30 for _ in range(30)]
for i in range(30):
    for j in range(30):
        if i == 1:
            dp[i][j] = j
        else:
            if i == j:
                dp[i][j] = 1
            elif i < j:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
for _ in range(T):
    n, m = list(map(int, input().split()))
    print(dp[n][m])
    
#-------------------------------
# python에서 제공하는 factorial 함수 사용 
import sys
from math import factorial

input = sys.stdin.readline

N = int(input())

for i in range(N):
    x, y = map(int, input().split())
    print(int(factorial(y)/(factorial(y-x)*factorial(x))))