"""
1. 아이디어
- while문으로, 특정조건 종료될 때까지 반복
- 4방향을 for문으로 탐색
- 더이상 탐색 불가능할 경우, 뒤로 한칸 후진
2. 시간복잡도
- O(NM) : 50^2 = 2500 < 2억
3. 자료구조
- map : int[][]
- 로봇청소기 위치, 방향, 전체 청소한 곳 수
"""

# 알고리즘 문제의 특징은 하라는 것만 잘 구현하면 된다.

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
y, x, d = map(int, input().split())
map = [list(map(int,input().split())) for _ in range(N)]

# 개수 변수
cnt = 0

# 방향벡타
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while 1:
    # 현재 위치를 청소한다. -> 현재 위치가 빈칸일때만 청소
    if map[y][x] == 0 :
       map[y][x] = 2
       cnt += 1
    check = False
    for i in range(1, 5):
        ny = y + dy[d-i]
        nx = x + dx[d-i]

        if 0 <= ny < N and 0 <= nx < M:
            if map[ny][nx] == 0:
                d = (d+4-i) % 4
                y = ny
                x = nx
                check = True
                break
    if check == False:
        ny = y - dy[d]
        nx = x - dx[d]

        if 0 <= ny < N and 0 <= nx < M:
            if map[ny][nx] == 1:
                break
            else:
                y = ny
                x = nx

        else:
            break

print(cnt)


