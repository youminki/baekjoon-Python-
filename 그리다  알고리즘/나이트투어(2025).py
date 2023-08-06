"""https://www.acmicpc.net/problem/2025"""
# 나이트 투어 2025
# 1. 체스판의 한 위치에서 시작한다.
# 2. knight의 현위치에서 knight가 이동할 수 있는 위치를 찾아서 좌표로 모두 표시한다.
# 3. knight가 이동 가능한 위치에서 다음 단계에서 knight가 이동할 수 있는 위치의 개수가 가장 적은 위치로 이동한다.
# 4. 모든 칸을 반복할 때까지 위 과정을 반복한다.
def knight_tour(n, x, y):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    chess = (x - 1,   y - 1)
    board[chess[0]][chess[1]] = 1
    path = [chess]

    def get_degree(x, y):
        degree = 0
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
                degree += 1
        return degree

    for i in range(2, n * n + 1):
        min_degree = n + 1
        next_chess = ()
        for move in moves:
            nx = chess[0] + move[0]
            ny = chess[1] + move[1]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
                c_degree = get_degree(nx, ny)
                if c_degree < min_degree:
                    min_degree = c_degree
                    next_chess = (nx, ny)
        if min_degree == n + 1:
            return False
        board[next_chess[0]][next_chess[1]] = i
        chess = next_chess
        path.append(chess)
    return path

n = int(input())
x,y = map(int, input().split())
path = knight_tour(n, x,  y)
if path:
    for x, y in path:
        print(x + 1, y + 1)
else:
    print(-1, -1)

#--------------------------------------------
# 입력값 받기
N = int(input())  # 체스판 크기 N
x, y = map(int, input().split())  # 시작 위치 x, y (1부터 시작)

# 시작 위치를 0부터 시작하도록 변경
x, y = x - 1, y - 1

# 나이트가 이동 가능한 8가지 방향의 상대적인 좌표 변화값
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]

# 해당 위치가 체스판 안에 있는지 확인하고, 방문한 적이 없는지 확인하는 함수
def visited(y, x, arr):
    return 0 <= x < N and 0 <= y < N and arr[y][x] == -1

# 나이트 투어 경로를 찾는 함수
def road(index, y, x, arr):
    if index == N * N:
        arr[y][x] = index - 1
        return True

    min_val = 8
    min_idx = -1
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        val = 0
        if visited(ny, nx, arr):
            for j in range(8):
                ty = ny + dy[j]
                tx = nx + dx[j]
                if visited(ty, tx, arr):
                    val += 1
            if min_val > val:
                min_val = val
                min_idx = i

    ny = y + dy[min_idx]
    nx = x + dx[min_idx]
    if visited(ny, nx, arr):
        arr[y][x] = index - 1
        if road(index + 1, ny, nx, arr):
            return True
        else:
            arr[y][x] = -1
    return False

# NxN 크기의 체스판 생성 및 초기화 (-1은 방문하지 않은 상태)
arr = [[-1 for _ in range(N)] for _ in range(N)]
arr[y][x] = 0

# trace 배열 생성, 경로 정보를 저장할 리스트
trace = [[0 for _ in range(2)] for _ in range(N * N)]

# road 함수를 호출하여 나이트 투어 경로를 찾고 출력
if road(1, y, x, arr):
    # trace 배열에 경로 정보 저장
    for i in range(N):
        for j in range(N):
            trace[arr[i][j]][1] = i
            trace[arr[i][j]][0] = j
    # 경로 정보 출력
    for i in range(N * N):
        print(trace[i][0] + 1, trace[i][1] + 1)
else:
    # 경로가 없을 경우 -1 -1 출력
    print("-1 -1")
