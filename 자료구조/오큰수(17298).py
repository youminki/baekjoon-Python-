# 오큰수(17298).py
"""https://www.acmicpc.net/problem/17298"""
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
result = [-1] * n
stack = []
for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        result[stack.pop()] = a[i]
    stack.append(i)
print(" ".join(map(str, result)))
    
    
# ----------------------------------------------
# 주석있는 버젼

import sys

n = int(sys.stdin.readline()) # 사용자로부터 정수를 입력받아 변수 n에 저장합니다.
a = list(map(int, sys.stdin.readline().split())) # 사용자로부터 공백으로 구분된 정수들을 입력받아 리스트 a에 저장합니다.
result = [-1] * n # 결과 리스트 result을 n개의 -1로 초기화합니다.
stack = []  # 인덱스를 저장하는 스택을 초기화합니다.

for i in range(n): # 리스트 a의 각 요소에 대해 반복합니다.
    while stack and a[stack[-1]] < a[i]: # 스택이 비어있지 않고, 스택의 최상단 요소에 해당하는 리스트 a의 값이 현재 요소보다 작을 때까지 반복합니다.
        result[stack.pop()] = a[i]  # 스택의 최상단 요소에 해당하는 인덱스를 결과 리스트에 저장하고 스택에서 제거합니다.
    stack.append(i)  # 현재 요소의 인덱스를 스택에 추가합니다.
print(" ".join(map(str, result))) # 결과 리스트의 각 요소를 공백으로 구분하여 문자열로 변환하고 출력합니다.
