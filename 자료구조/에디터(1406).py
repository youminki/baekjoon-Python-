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


#------------------------------------------
#주석 추가 코드
from sys import stdin

# 입력으로 주어진 문자열을 스택으로 사용할 리스트 stack1에 저장합니다.
stack1 = list(stdin.readline().strip())
# 별도의 스택인 stack2를 생성합니다.
stack2 = []

# 명령어 개수를 입력받습니다.
n = int(input())

# 각 명령어를 처리합니다.
for line in stdin:
    if line[0] == 'L' and stack1:  # 커서를 왼쪽으로 옮깁니다.
        stack2.append(stack1.pop())  # stack1의 가장 오른쪽 문자를 stack2로 이동시킵니다.
    elif line[0] == 'D' and stack2:  # 커서를 오른쪽으로 옮깁니다.
        stack1.append(stack2.pop())  # stack2의 가장 왼쪽 문자를 stack1로 이동시킵니다.
    elif line[0] == 'B' and stack1:  # 커서 왼쪽에 있는 문자를 삭제합니다.
        stack1.pop()  # stack1에서 가장 오른쪽 문자를 삭제합니다.
    elif line[0] == 'P':  # 문자를 추가합니다.
        stack1.append(line[2])  # 명령어의 세 번째 문자를 stack1에 추가합니다.

# stack1과 stack2를 합친 뒤, stack2를 뒤집어서 이어붙여서 결과 문자열을 생성합니다.
result = ''.join(stack1 + stack2[::-1])
# 결과 문자열을 출력합니다.
print(result)