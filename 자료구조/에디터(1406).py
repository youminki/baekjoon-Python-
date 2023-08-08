# 에디터(1406).py
"""https://www.acmicpc.net/problem/1406"""
from sys import stdin

stack1 = list(stdin.readline().strip())
stack2 = []
n = int(input())

for line in stdin:
    if line[0] == 'L' and stack1:
        stack2.append(stack1.pop())
    elif line[0] == 'D' and stack2:
        stack1.append(stack2.pop())
    elif line[0] == 'B' and stack1:
        stack1.pop()
    elif line[0] == 'P':
        stack1.append(line[2])
print(''.join(stack1 +stack2[::-1]))


