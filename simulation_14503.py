"""
1. 아이디어
- while문으로, 특정조건 종료될 때까지 반복
- 4방향을 for문으로 탐색
- 더이상 탐색 불가능할 경우, 뒤로 한칸 후진
- 후진이 불가능할 경우 종료
2. 시간복잡도
- O(NM) : 50^2 = 2500 < 2억
- 지도가 n*m 최대는 칸의 개수
- 시간 복잡도에서 상수가 곱해지는 것은 생략할 수 있다.
3. 자료구조
- map : int[][]
- 로봇청소기 위치, 방향, 전체 청소한 곳 수
"""

# 시뮬레이션 문제의 특징은 하라는 것만 잘 구현하면 된다.

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
y, x, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

# 방향 설정
dy = [-1,0,1,0]
dx = [0,1,0,-1]

cnt = 0

while 1:

    # 현 위치에서 청소
    if map[y][x] == 0:
        map[y][x] = 2
        cnt += 1

    # 방향을 바꿔 가면서 check
    switch = False
    for i in range(1, 5):
        # 왼쪽으로 돌기 때문에 방향은 d-i 이다
        ny = y + dy[d-i]
        nx = x + dx[d-i]

        # 무조건 방향이나 좌표의 이동이 있으면 해당 map 범위 안에 있는지 체크를 해야한다.
        if 0<=ny<n and 0<=nx<m:
            if map[ny][nx] == 0:
                d = (d-i+4)%4
                y = ny
                x = nx
                switch = True
                break

    # 네 방향을 돌았는데도 바꿀곳이 없으면 작동
    if not switch:
        # 뒤를 확인해 봐야 한다.
        ny = y - dy[d]
        nx = x - dx[d]

        # 좌표의 이동이 있었으니 해당 map에 있는지 체크를 해야한다.
        if 0<=ny<n and 0<=nx<m:
            # 벽이면 종료
            if map[ny][nx] == 1:
                break
            else:
                y = ny
                x = nx
        else:
            break

print(cnt)





