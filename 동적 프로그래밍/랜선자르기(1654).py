""" https://www.acmicpc.net/problem/1654"""

import sys

# 입력 받기
K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]  # 랜선의 길이 정보 입력 받기
start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2  # 중간 위치 계산
    count = 0  # 랜선 수 초기화
    for i in lan: # 주어진 랜선들을 중간 길이로 잘랐을 때 몇 개로 나눌 수 있는지 계산
        count += i // mid  # 분할된 랜선 수 추가
    if count >= N:  # 찾고자 하는 랜선의 개수 이상인 경우
        start = mid + 1  # 중간 위치 이후를 탐색
    else:
        end = mid - 1  # 중간 위치 이전을 탐색
print(end)
