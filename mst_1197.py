"""
1. 아이디어
 - MST 기본문제, 외우기
 - 간선을 인접리스트에 집어넣기
 - 힙에 시작접 넣기
 - 힙이 빌때까지 다음의 작업을 반복
    - 힙의 최소값 꺼내서, 해당 노드 방문 안했다면
        - 방문표시, 해당 비용 추가, 연결된 간선들 힙에 넣어주기

2. 시간 복잡도
- MST : O(ElgE)

3. 자료구조
- 간선 저장되는 인접리스트 : (무게, 노드번호) --> 무게에 따라 힙을 정렬해야하기 때문이다.
- 힙 : (무게, 노드번호)
- 방문 여부 : bool[]
- MST 결과값 : int
"""

import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
# 미리 모든 노드에 대해서 edge를 초기화해야 한다. + 꼭지점 번호에 바로 접근을 하기 위해 개수에 +1을 한만큼 리스트를 만든다.
edge_list = [[] for _ in range(V+1)]
# 인접 리스트 만들기 끝
for _ in range(E):
    A, B, C = map(int, input().split())
    edge_list[A].append([C,B])
    edge_list[B].append([C,A])

# 노드의 방문 여부를 알기위해 check_list를 만든다.
check = [False] * (V+1)

# heap을 아예 만든다. 그런데 힙에는 처음 값이 입력되어 있다.
# 그리고 힙은 배열의 첫번째 요소를 기준으로 정렬하므로 첫 번째 값에 비용을 넣어준다.
heap = [[0,1]]
rs = 0
while heap:
    w, each_node = heapq.heappop(heap)
    if check[each_node] == False:
        check[each_node] = True
        rs += w
        for next_node in edge_list[each_node]:
            if check[next_node[1]] == False:
                heapq.heappush(heap, next_node)
print(rs)