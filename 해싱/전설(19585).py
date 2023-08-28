# 전설(19585).py
""" https://www.acmicpc.net/problem/19585 """

import sys

input = sys.stdin.readline
C,N = map(int,input().split())
colors = {}
for _ in range(C):
    now = colors
    for c in input().strip():
        if not now.get(c):
            now[c] = {}
        now = now[c]
    now[0] = 1
names = {input().strip() for i in range(N)}

def hash(word):
    now = colors
    for i in range(len(word)):
        if now.get(0) and word[i:] in names:
            return True
        if not now.get(word[i]):
            return False
        now = now[word[i]]

for _ in range(int(input())):
    print("Yes" if hash(input().strip()) else "No")


# ---------------------------------------------------
# 주석버전

import sys

input = sys.stdin.readline

# 입력 받기
C, N = map(int, input().split())  # C: 색상 수, N: 이름 수
colors = {}  # 각 색상을 트리 형태로 저장할 딕셔너리
for _ in range(C):
    now = colors  # 현재 상태 초기화
    for c in input().strip():  # 각 색상을 문자 단위로 분리하여 처리
        if not now.get(c):  # 현재 문자가 현재 상태에 없으면
            now[c] = {}  # 새로운 상태(딕셔너리)를 만들어서 추가
        now = now[c]  # 다음 상태로 이동
    now[0] = 1  # 색상의 끝을 나타내는 0을 추가하여 표시

names = {input().strip() for i in range(N)}  # names 집합에 이름들을 저장

# 해시 함수를 사용하여 주어진 단어가 트리에 있는지 확인하는 함수
def hash(word):
    now = colors
    for i in range(len(word)):
        if now.get(0) and word[i:] in names:
            return True  # 주어진 단어가 트리에 존재하면 True 반환
        if not now.get(word[i]):
            return False  # 현재 문자가 트리에 없으면 False 반환
        now = now[word[i]]  # 다음 상태로 이동

# 각 테스트 케이스에 대해 결과 출력
for _ in range(int(input())):
    print("Yes" if hash(input().strip()) else "No")



# ---------------------------------------------------
# 19585
# python set 돌리기

color = set()
name = set()
C, N = map(int, input().split())

for _ in range(C) :
    color.add(input())
for _ in range(N) :
    name.add(input())

Q = int(input())
for _ in range(Q) :
    X = input()
    
    ans = "No"
    for i in range(max(1, len(X) - 1005), min(len(X), 1005)) :
        if X[:i] in color and X[i:] in name :
            ans = "Yes"
            break
    print(ans)