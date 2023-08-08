# 스택(10828)
"""https://www.acmicpc.net/problem/10828"""
import sys

input = sys.stdin.readline
s = []
for _ in range(int(input())):
    n = list(input().split())
    if n[0] == "push":
        s.append(n[1])
    if n[0] == "pop":
        print(s.pop() if s else -1)
    if n[0] == "size":
        print(len(s))
    if n[0] == "empty":
        print(1 if not s else 0)
    if n[0] == "top":
        print(s[-1] if s else -1)
        
#------------------------------------------
#주석 추가 코드
import sys

# 입력 함수를 sys.stdin.readline으로 지정합니다.
input = sys.stdin.readline

# 빈 리스트 s를 생성하여 스택(Stack)으로 사용합니다.
s = []

# 입력으로 주어진 횟수만큼 반복합니다.
for _ in range(int(input())):
    # 입력을 공백을 기준으로 분리하여 리스트 n에 저장합니다.
    n = list(input().split())
    
    # 명령어가 "push"인 경우
    if n[0] == "push":
        s.append(n[1])  # 스택 s에 값을 추가합니다.
    
    # 명령어가 "pop"인 경우
    if n[0] == "pop":
        print(s.pop() if s else -1)  # 스택 s에서 가장 위에 있는 값을 꺼내어 출력합니다. 비어있을 경우 -1을 출력합니다.
    
    # 명령어가 "size"인 경우
    if n[0] == "size":
        print(len(s))  # 스택 s의 길이(크기)를 출력합니다.
    
    # 명령어가 "empty"인 경우
    if n[0] == "empty":
        print(1 if not s else 0)  # 스택 s가 비어있으면 1, 비어있지 않으면 0을 출력합니다.
    
    # 명령어가 "top"인 경우
    if n[0] == "top":
        print(s[-1] if s else -1)  # 스택 s의 가장 위에 있는 값을 출력합니다. 비어있을 경우 -1을 출력합니다.
