# 단어 뒤집기(9093).py
"""https://www.acmicpc.net/problem/9093"""
n = int(input())  # 테스트 케이스의 개수

# 각 테스트 케이스마다 반복 수행
for i in range(n):
    string = input()  # 단어 또는 문장 입력 받기
    string += ""  # 문자열 마지막에 빈 문자열("") 추가하여 마지막 단어 뒤집기 위해
    stack = []  # 뒤집기를 위한 스택 선언
    # 문자열 순회
    for j in string:
        if j != " ":  # 공백 문자가 아닌 경우 (단어인 경우)
            stack.append(j)  # 스택에 문자 추가
        else:  # 공백 문자인 경우 (단어가 끝난 경우)
            while stack:  # 스택이 비어있지 않은 동안 반복
                print(stack.pop(), end='')  # 스택에서 문자를 빼고 출력 (단어 뒤집기)
            print(' ', end=' ')  # 띄어쓰기 출력 (단어 사이 공백 처리)

#----------------------------------------
# 파이썬에서 지원하는 함수를 이용

n = int(input())  # 테스트 케이스의 개수
for i in range(n): # 각 테스트 케이스마다 반복 수행
    string = list(input().split())  # 공백을 기준으로 단어들을 리스트로 입력 받기
    for j in string: # 각 단어를 뒤집어서 출력
        print(j[::-1], end=' ')  # 문자열을 뒤집어 출력 (공백으로 구분하여 출력)
