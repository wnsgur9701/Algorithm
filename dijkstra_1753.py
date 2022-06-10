"""
1. 아이디어
- 한점시작, 모든 거리 : 다익스트라
- 간선, 인접리스트 저장
- 거리배열 무한대 초기화
- 시작점 : 거리배열 0, 힙에 넣어주기
- 힙에서 빼면서 다음의 것들 수행
    - 최시값인지 먼저 확인
    - 간선을 타고 간 비용이 더 작으면 갱신

2. 시간 복잡도
- 다익스트라 : O(ElgV)
     - E : 3e5
     - V : 2e4, lgV ~= 20
     - ElgV

3. 변수
- 힙 : (비용, 노드번호)
- 거리 배열 : 비용 : int[]
- 간선 저장, 인접리스트 : (비용, 노드번호[])
"""

import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
INF = sys.maxsize
node_list = [[] for _ in range(V+1)]
dist = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    node_list[u].append([w,v])

heap = [[0, K]]
dist[K] = 0

while heap:
    ew, ev = heapq.heappop(heap)
    if dist[ev] != ew: continue
    for nw, nv in node_list[ev]:
        if dist[nv] > nw + ew:
            dist[nv] = nw + ew
            heapq.heappush(heap, [dist[nv], nv])

for i in range(1, V+1):
    if dist[i] == INF: print("INF")
    else: print(dist[i])