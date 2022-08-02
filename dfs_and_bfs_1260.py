"""
1. 아이디어
    - 노드의 개수 만큼 배열 초기화(이차원 배열)
    - 배열 내부의 값들 sort
    - dfs 실행
        - 재귀적으로 호출하며 실행
    - bfs 실행
        - 큐를 사용하여 큐에 있는 값이 끝날때 까지 실행

2. 자료구조
    - 방문 -> bool[][]
    - graph -> int[][]
"""
import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)


# 정점 입력 받아서 graph에 넣기
for i in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 그래프 순회 하면서 정렬
for i in range(1,N+1):
    graph[i].sort()

# 재귀적으로 호출을 해서 print 만 한다.
def dfs(v):
    visited_dfs[v] = True
    print(v, end=" ")
    for nv in graph[v]:
        if not visited_dfs[nv]:
            dfs(nv)

# 조건에 맞으면 True를 해주고 큐에 넣는다.
def bfs(v):
    q = deque()
    q.append(v)
    visited_bfs[v] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for nv in graph[v]:
            if not visited_bfs[nv]:
                visited_bfs[nv] = True
                q.append(nv)

dfs(V)
print()
bfs(V)





