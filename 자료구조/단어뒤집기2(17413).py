# 단어뒤집기2(17413).py
"""https://www.acmicpc.net/problem/17413"""
import sys

input = list(map(str, sys.stdin.readline().strip()))

result = ""
word = ""
reverse = True

for i in input:
    if i == '<':
        reverse = False
        result += word
        word = i

    elif i == '>':
        reverse = True
        result += (word + '>')
        word = ""

    elif i == ' ':
        result += word + i
        word = ""

    elif reverse:
        word = i + word

    else:
        word += i

result += word
print(result)

#------------------------------------------------
import sys

input = list(map(str, sys.stdin.readline().strip()))# 표준 입력으로부터 한 줄을 읽어와서 문자열의 리스트로 변환합니다.
result = "" # 결과 문자열을 초기화합니다.
word = "" # 현재 처리 중인 단어를 나타내는 변수입니다.
reverse = True # '<'와 '>' 사이의 문자열을 역순으로 만들지 여부를 나타내는 변수입니다.

for i in input: # 입력으로 받은 각 문자에 대해 반복합니다.
    if i == '<': # 입력으로 받은 각 문자에 대해 반복합니다.
        # 역순으로 만들지 않도록 설정하고, 현재까지 만들어진 단어를 결과에 추가하고 초기화합니다.
        reverse = False
        result += word
        word = i
    elif i == '>':# '>'를 만났을 때의 처리입니다.
        # 역순으로 만들도록 설정하고, 현재까지 만들어진 단어와 '>'를 결과에 추가하고 초기화합니다.
        reverse = True
        result += (word + '>')
        word = ""
    elif i == ' ':# 공백을 만났을 때의 처리입니다.
        # 현재까지 만들어진 단어와 공백을 결과에 추가하고 초기화합니다.
        result += word + i
        word = ""
    elif reverse: # 역순으로 만들지 않을 때의 처리입니다.
        # 현재 문자를 단어의 앞에 추가합니다.
        word = i + word
    else: # 역순으로 만들지도 않고, 공백도 아닐 때의 처리입니다.
        # 현재 문자를 단어에 추가합니다.
        word += i
result += word # 남은 단어를 결과에 추가합니다.
print(result)
