"""
1. 아이디어
    - 이중 for문 -> 1이거나 check하지 않았다면 cnt + 1 하고 bfs
    - bfs -> 넓이 list에 추가
2. 시간 복잡도
    - bfs -> O(V+E)
    - V : 노드의 수
        * 행 x 열  -> 25 x 25 = 625
    - E : 간선의 수
        * 최대 간선의 수 4V = 4 x 625 = 2500
    - V + E = 3125 < 2억 연산 가능

3. 자료 구조
    그래프 저장 : int[][]
    방문 여부 : bool[][]
    결과 리스트 : int[]
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

map = [list(map(int, input().strip())) for _ in range(n)]
check = [[False] * n for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y: int, x: int):
    rs = 1
    q = deque()
    q.append((y,x))
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<n:
                if map[ny][nx] == 1 and check[ny][nx] == False:
                    check[ny][nx] = True
                    rs += 1
                    q.append((ny,nx))
    return rs

cnt = 0
result_list = []
for i in range(n):
    for j in range(n):
        if map[i][j] == 1 and check[i][j] == False:
            check[i][j] = True
            cnt += 1
            size = bfs(i,j)
            result_list.append(size)

print(cnt)
result_list.sort()
for result in result_list:
    print(result)

