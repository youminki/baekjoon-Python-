#큐(10845).py
"""https://www.acmicpc.net/problem/10845"""
import sys

input = sys.stdin.readline
q = []
for _ in range(int(input())):
    n = list(input().split())
    if n[0] == "push":
        q.append(n[1])
    if n[0] == "pop":
        print(q.pop(0) if q else -1)
    if n[0] == "size":
        print(len(q))
    if n[0] == "empty":
        print(1 if not q else 0)
    if n[0] == "front":
        print(q[0] if q else -1)
    if n[0] == "back":
        print(q[-1] if q else -1)
