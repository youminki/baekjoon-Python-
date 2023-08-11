# 쇠막대기(10799).py
"""https://www.acmicpc.net/problem/10799"""
"""
예제 입력 1
()(((()())(())()))(())
예제 출력 1
17
예제 입력 2
(((()(()()))(())()))(()())
예제 출력 2
24
"""

input = input()
stack = []
count = 0
for i in range(len(input)):
    if input[i] == "(":
        stack.append("(")
    else:
        if input[i - 1] == "(":
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1
print(count)




#-----------------------------------
#주석 o
input = input()  # 사용자로부터 문자열을 입력받습니다.
stack = []  # 괄호 문자열을 처리하기 위한 스택을 초기화합니다.
count = 0  # 괄호 쌍의 개수를 세기 위한 변수를 초기화합니다.
# 입력받은 문자열의 각 문자에 대해서 반복합니다.
for i in range(len(input)):
    if input[i] == "(":  # 현재 문자가 열린 괄호 "(" 인 경우
        stack.append("(")  # 스택에 열린 괄호를 추가합니다.
    else:  # 현재 문자가 닫힌 괄호 ")" 인 경우
        if input[i - 1] == "(":  # 이전 문자가 열린 괄호인지 확인합니다.
            stack.pop()  # 이전 열린 괄호를 스택에서 제거합니다.
            count += len(stack)  # 스택에 남아있는 열린 괄호의 개수를 괄호 쌍의 개수에 더합니다.
        else:
            stack.pop()  # 스택에서 가장 최근의 열린 괄호를 제거합니다.
            count += 1  # 괄호 쌍의 개수를 1 증가시킵니다.

# 괄호 쌍의 총 개수를 출력합니다.
print(count)
