# 1,2,3더하기(9095).py
"""https://www.acmicpc.net/problem/9095"""

import sys

input = sys.stdin.readline
n = int(input())
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = sum(dp[i-3:i])
    
n = int(input())
for _ in range(n):
    print(dp[int(input())])

#----------------------------------
import sys

input = sys.stdin.readline
dp = [0] * 11 # n의값이 11보다 작다고 명시되어 있으므로 n의 범위는 n < 11이다.
dp[1] = 1 # dp[1]은 1을 가지고 조합할수 있는 계산 수는 (1) = 1이다.
dp[2] = 2 # dp[2]은 1, 2을 가지고 조합할수 있는 계산 수는 (1+1),(2) = 2이다.
dp[3] = 4 # dp[3]은 1,2,3을 가지고 조합할수 있는 계산 수는 (1+1+1),(1+2),(2+1),(3) = 4이다.
# dp[4] = 7 # dp[4]은 (1+1+1+1), (1+1+2), (1+2+1), (1+3), (2+1+1), (2+2), (3+1)
# dp[5] = 13 # dp[5]은 (1+1+1+1+1), (1+1+1+2), (1+1+2+1), (1+1+3), (1+2+1+1), (2+1+1+1), (1+2+2), (2+1+2), (2+2+1), (1+3+1), (3+1+1), (2+3), (3+2)
for i in range(4, 11): # 1~3은 앞에서 계산했으므로 4부터 계산한다.
    dp[i] = sum(dp[i-3:i])
    
n = int(input())
for _ in range(n):
    print(dp[int(input())])
