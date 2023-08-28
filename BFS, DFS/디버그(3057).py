# 입력
n, m = map(int, input().split())
A = [list(input().strip()) for _ in range(n)]

# 위 아래 왼쪽 오른쪽 비트열을 저장할 배열
v = [[[0] * 4 for _ in range(m)] for _ in range(n)]

# 아래, 오른쪽 방향 비트열을 계산하는 함수
def compute_right_down(n, m, A, v):
    for i in range(1, n):
        for j in range(1, m):
            v[i][j][1] = (v[i - 1][j][1] << 1) | int(A[i][j])
            v[i][j][3] = (v[i][j - 1][3] << 1) | int(A[i][j])
            # 정수 오버플로우 방지를 위해 64비트로 제한
            v[i][j][1] &= ((1 << 64) - 1)
            v[i][j][3] &= ((1 << 64) - 1)

# 위, 왼쪽 방향 비트열을 계산하는 함수
def compute_left_up(n, m, A, v):
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            v[i][j][0] = (v[i + 1][j][0] << 1) | int(A[i][j])
            v[i][j][2] = (v[i][j + 1][2] << 1) | int(A[i][j])
            # 정수 오버플로우 방지를 위해 64비트로 제한
            v[i][j][0] &= ((1 << 64) - 1)
            v[i][j][2] &= ((1 << 64) - 1)

# 아래, 오른쪽 방향 비트열 계산
compute_right_down(n, m, A, v)
compute_left_up(n, m, A, v)

# 가장 큰 정사각형 킬러의 크기를 찾는 함수
def find_largest_square_killer(n, m, A, v):
    largest_size = -1

    for i in range(n):
        for j in range(m):
            size = 1
            ok = True

            while i + size <= n and j + size <= m and ok:
                x = v[i][j + size - 1][3]
                y = v[i + size - 1][j][1]

                if x != y:
                    ok = False
                else:
                    size += 1

            largest_size = max(largest_size, size - 1)

    return largest_size

# 가장 큰 정사각형 킬러의 크기 찾기
largest_size = find_largest_square_killer(n, m, A, v)

# 출력
print(largest_size)
