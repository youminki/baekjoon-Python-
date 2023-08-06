# 괄호(9012).py
"""https://www.acmicpc.net/problem/9012"""

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    K = sys.stdin.readline().strip()
    sum = 0
    for check in K:
        if check == '(':    # 왼쪽 괄호면 +1
            sum+=1
        elif check == ')':   # 오른쪽 괄호면 -1
            sum -= 1
        if sum < 0:    # 이떄 만약 0보다 작아지면 불균형 발생하므로 NO 출력후 break
            print('NO')
            break
    if sum > 0:    # 만약 (((((만 나와서 양수가 된 경우도 불균형이 발생한 케이스이기 떄문에 NO 출력
        print('NO')
    elif sum == 0:    # 정상적으로 짝이 맞는 경우는 합격 (단 elif문을 사용해 우선 검증을 실시 해야 한다.)
        print('YES')

#------------------------------------
# 파이썬에서 지원하는 함수를 이용
import sys

n = sys.stdin.readlines()[1:]
for check in n:
	check = check.rstrip()
	while '()' in check:
		check = check.replace('()', '')
	
	if check:
		print('NO')
	else:
		print('YES')