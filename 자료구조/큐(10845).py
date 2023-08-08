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

#------------------------------------------
#주석 추가 코드
# sys 모듈을 불러옵니다.
import sys

# 입력 함수를 sys.stdin.readline으로 지정합니다.
input = sys.stdin.readline

# 빈 리스트 q를 생성하여 큐로 사용합니다.
q = []

# 입력으로 주어진 횟수만큼 반복합니다.
for _ in range(int(input())):
    # 입력을 공백을 기준으로 분리하여 리스트 n에 저장합니다.
    n = list(input().split())
    
    # 명령어가 "push"인 경우
    if n[0] == "push":
        q.append(n[1])  # q 리스트에 값을 추가합니다.
    
    # 명령어가 "pop"인 경우
    if n[0] == "pop":
        print(q.pop(0) if q else -1)  # q 리스트의 가장 앞에 있는 값을 꺼내어 출력합니다. 비어있을 경우 -1을 출력합니다.
    
    # 명령어가 "size"인 경우
    if n[0] == "size":
        print(len(q))  # q 리스트의 길이(크기)를 출력합니다.
    
    # 명령어가 "empty"인 경우
    if n[0] == "empty":
        print(1 if not q else 0)  # q 리스트가 비어있으면 1, 비어있지 않으면 0을 출력합니다.
    
    # 명령어가 "front"인 경우
    if n[0] == "front":
        print(q[0] if q else -1)  # q 리스트의 가장 앞에 있는 값을 출력합니다. 비어있을 경우 -1을 출력합니다.
    
    # 명령어가 "back"인 경우
    if n[0] == "back":
        print(q[-1] if q else -1)  # q 리스트의 가장 뒤에 있는 값을 출력합니다. 비어있을 경우 -1을 출력합니다.
