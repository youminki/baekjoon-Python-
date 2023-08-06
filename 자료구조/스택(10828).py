# 스택(10828)
"""https://www.acmicpc.net/problem/10828"""
import sys

input = sys.stdin.readline
stack = []
for _ in range(int(input())):
    n = list(input().split())
    if n[0] == "push":
        stack.append(n[1])
    if n[0] == "pop":
        print(stack.pop() if stack else -1)
    if n[0] == "size":
        print(len(stack))
    if n[0] == "empty":
        print(1 if not stack else 0)
    if n[0] == "top":
        print(stack[-1] if stack else -1)