"""
1. 아이디어
- for 문을 돌면서 각각 계산
- 몫을 구해서 업데이트
- k도 없데이트(나머지)
- 만약 k가 0이 된다면 멈춘다.
2. 시간복잡도
- O(N)
3. 자료구조
- 동전 금액 : int[]
- 동전 사용 cnt : int
- 남은 금액 : int
"""

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coin_list = [int(input()) for _ in range(N)]
print(coin_list)

coin_list.reverse()

cnt = 0
for coin in coin_list:
    cnt += K // coin
    K = K % coin
    if K == 0:
        break

print(cnt)