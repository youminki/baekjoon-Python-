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
        
        
#------------------------------------------
#주석 추가 코드
import sys

# 입력 함수를 sys.stdin.readline으로 지정합니다.
input = int(sys.stdin.readline())

# 빈 리스트 d를 생성하여 덱(Deque)으로 사용합니다.
d = []

# 입력으로 주어진 횟수만큼 반복합니다.
for i in range(input):
    # 입력을 공백을 기준으로 분리하여 리스트 n에 저장합니다.
    n = sys.stdin.readline().split()
    
    # 명령어가 "push_front"인 경우
    if n[0] == "push_front":
        d.insert(0, n[1])  # 덱의 가장 앞에 값을 추가합니다.
    
    # 명령어가 "push_back"인 경우
    if n[0] == "push_back":
        d.append(n[1])  # 덱의 가장 뒤에 값을 추가합니다.
    
    # 명령어가 "pop_front"인 경우
    if n[0] == "pop_front":
        print(d.pop(0) if d else -1)  # 덱의 가장 앞에 있는 값을 꺼내어 출력합니다. 비어있을 경우 -1을 출력합니다.
    
    # 명령어가 "pop_back"인 경우
    if n[0] == "pop_back":
        print(d.pop(-1) if d else -1)  # 덱의 가장 뒤에 있는 값을 꺼내어 출력합니다. 비어있을 경우 -1을 출력합니다.
    
    # 명령어가 "size"인 경우
    if n[0] == "size":
        print(len(d))  # 덱의 길이(크기)를 출력합니다.
    
    # 명령어가 "empty"인 경우
    if n[0] == "empty":
        print(0 if d else 1)  # 덱이 비어있으면 1, 비어있지 않으면 0을 출력합니다.
    
    # 명령어가 "front"인 경우
    if n[0] == "front":
        print(d[0] if d else -1)  # 덱의 가장 앞에 있는 값을 출력합니다. 비어있을 경우 -1을 출력합니다.
    
    # 명령어가 "back"인 경우
    if n[0] == "back":
        print(d[-1] if d else -1)  # 덱의 가장 뒤에 있는 값을 출력합니다. 비어있을 경우 -1을 출력합니다.
