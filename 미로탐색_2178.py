import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().strip())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(y,x):
    q = deque()
    q.append((y,x))
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1:
                    q.append((ny,nx))
                    map[ny][nx] = map[y][x] + 1

bfs(0,0)
print(map[n-1][m-1])

