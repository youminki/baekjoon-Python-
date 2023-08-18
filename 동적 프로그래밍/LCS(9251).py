# LCS(9251).py
""" https://www.acmicpc.net/problem/9251 """
"""import sys

input = sys.stdin.readline
n1 = input()
n2 = input()
dp = [[0 for _ in range(1001)] for _ in range(1001)]
# print(dp)

for i in range(1, len(n1) + 1):
    for j in range(1, len(n2) + 1):
        if n2[i - 1]: ==  n1[j - 1]
            dp[i][j] = dp[i - 1][j - 1] + 1
            continue
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(max(sum(dp, [])))

"""
n1 = input()
n2 = input()
dp = [[0 for _ in range(1001)] for _ in range(1001)]
for i in range(1, len(n2) + 1):
    for j in range(1, len(n1) + 1):
        if n1[j - 1] == n2[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            continue
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(max(sum(dp, [])))