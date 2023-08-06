#스택 수열(1874).py
"""https://www.acmicpc.net/problem/1874"""

import sys


def solution():
    input = sys.stdin.readline
    n = int(input())  # 8 (입력 개수)
    arr = [int(input()) for _ in range(n)]  # [4, 3, 6, 8, 7, 5, 2, 1] (입력 배열)
    stack = []  # increased_arr에서 pop한 요소를 담는 배열
    answer = []  # 연산자가 담길 배열 (정답배열)
    index = 0  # 일치시켜야 하는 수열의 인덱스를 가리킴

    for i in range(1, n + 1):  # 1 ~ 8
        # 비교하려면 무조건 스택에 하나는 넣어야 함
        stack.append(i)
        answer.append('+')
        # 스택에 원소가 존재하고, 스택의 마지막 원소와
        # 입력받은 원소 배열의 index번째 원소가 같을 경우
        while stack and stack[-1] == arr[index]:
            stack.pop()
            answer.append('-')
            index += 1
    # for문이 끝났는데 stack에 원소가 남아있다면,
    # 순서가 맞지 않은 것이기 때문에 'NO'를 출력하고
    # 스택이 없으면 answer(연산자 배열)을 출력
    print('NO' if stack else '\n'.join(answer))
solution()

# 리스트 컴프리헨션 (List Comprehension)
# arr = [int(input()) for _ in range(n)]

# 동일
# arr = []
# for _ in range(n):
#     arr.append(int(input()))