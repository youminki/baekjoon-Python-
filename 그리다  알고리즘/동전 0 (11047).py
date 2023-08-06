#동전0 11047
"""https://www.acmicpc.net/problem/11047"""

import sys

n,k = map(int, sys.stdin.readline().split())  # 동전의 개수 n과 동전의 합 k를 입력받습니다.
coin = []
count = 0

# 여기서는 굳이 임시변수 i가 필요하지 않기때문에 반복문에 blank 처리를 한 것이다.
for _ in range(n):
  coin.append(int(sys.stdin.readline()))  # 동전의 값을 입력받아 리스트에 추가합니다.

coin.reverse()  # 동전의 값을 역순으로 정렬합니다.
for i in coin:
    count += k // i  # 동전의 값로 나눈 몫을 count에 더합니다. (해당 값의 동전 개수를 더합니다)
    k %= i  # 나머지를 k에 저장합니다. (해당 값의 동전을 사용한 후 남은 금액입니다)
print(count)   # 최종적으로 동전의 개수를 출력합니다.
