"""
# 문제 푸는 전략
1. 아이디어
- 2중 for => 값1 && 방문X => BFS
- BFS 돌면서 그림 개숫 +1 , 최대값을 갱신
2. 시간 복잡도
- BFS : O(V + E)
- V : 500 x 500 => 노드의 개수 (행과 열이 최대 5개이다)
- E : 4 x 500 x 500 => 한 노드에 연결된 최대의 간선은 4개 이기 떄문에 4V이다.
- V + E : 5 * 250000 = 100만 < 2억 >> 가능!
3. 자료구조
- 그래프 전체 지도 int[][]
- 방문 : bool[][]
- Queue(BFS)
"""
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
check = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y,x):
    rs = 1
    q = deque()
    q.append((y,x))
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and check[ny][nx] == False:
                    check[ny][nx] = True
                    rs += 1
                    q.append((ny,nx))
    return rs

cnt = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and check[j][i] == False:
            check[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j,i))



print(cnt)
print(maxv)

