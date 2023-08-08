# 덱(10866).py
"""https://www.acmicpc.net/problem/10866"""
import sys

input = int(sys.stdin.readline())
d = []
for i in range(input):
    n = sys.stdin.readline().split()
    if n[0] == "push_front":
        d.insert(0, n[1])
    if n[0] == "push_back":
        d.append(n[1])
    if n[0] == "pop_front":
        print(d.pop(0) if d else -1)
    if n[0] == "pop_back":
        print(d.pop(-1) if d else -1)
    if n[0] == "size":
        print(len(d))
    if n[0] == "empty":
        print(0 if d else 1)
    if n[0] == "front":
        print(d[0] if d else -1)
    if n[0] == "back":
        print(d[-1] if d else -1)