"""
1. 아이디어
- 2중 for, 갑 1 && 방문 x => dfs
2. 시간복잡도
- dfs : O(V + E)
- V , E : N^2, 4N^2
- V + E : 5N^2 ~= N^2 ~= 625 >> 가능
3. 자료구조
- 그래프 저장 int[][]
- 방문여부 bool[][]
- 결과값 int[][]
"""

import sys

input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]
check = [[False] * N for _ in range(N)]
result = []
each = 0

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def dfs(y,x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<N and 0<=nx<N:
            if map[ny][nx] == 1 and check[ny][nx] == False:
                check[ny][nx] = True
                dfs(ny,nx)



for j in range(N):
    for i in range(N):
        if map[j][i] == 1 and check[j][i] == False:
            check[j][i] = True
            each = 0
            dfs(j,i)
            result.append(each)

result.sort()
print(len(result))
for size in result:
    print(size)