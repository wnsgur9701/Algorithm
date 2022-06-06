# 그냥 for 문으로 했을 때 버전
"""
1. 아이디어
-> for문으로 각 숫자의 위치에서 이후 k개의 수를 더함
-> 이때마다 최대값으로 갱신

2. 시간 복잡도
-> for문 : O(N)
-> 각 위치에서 k개의 값 더함: O(K)
총 : O(NK)
여기서 n은 2이상 10만 이하 , k는 1과 n사이의 정수이다.
O(NK) -> 10만 * 10만 ~= 1e5 * 1e5 = 1e10(100억) > 2억
투포인터를 고려해보자
"""
# import sys
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
# num_list = list(map(int, input().split()))
#
# maxv = 0
#
# for i in range(n-k):
#     sum = 0
#     sum += num_list[i]
#     for j in range(i+1, i+k):
#         sum += num_list[j]
#     maxv = max(maxv, sum)
# print(sum)

########################## Two pointer 버전 ##############################
"""
1. 아이디어
- 투포인터를 활용
- for 문으로, 처음에 K개의 값을 저장
- 다음인덱스 더해주고, 이전 인덱스를 빼준다
- 이때마다 최대값을 갱신

2. 시간복잡도
- 원래는 O(2N) -> 더하기 빼기 떄문에
- 그러나 빅 O 표기법은 앞의 숫자를 무시하기 때문에 O(N)이라고 할 수 있다.

3. 자료구조
- 각 숫자들 N개 저장 배열 : int[]
    - 숫자들 최대 100 > INT가능 
- K개의 값을 저장변수 : int
    - 최대 : K * 100 = 1e5 * 100 = 1e7 > INT가능
- 최대값 : int
"""

import sys

input = sys.stdin.readline

n,k = map(int, input().split())
nums = list(map(int, input().split()))

each = 0
# 처음 k개의 수를 저장
for i in range(k):
    each += nums[i]
maxv = each
# 투포인터 적용
for i in range(k, n):
    each += nums[i]
    each -= nums[i-k]
    maxv = max(maxv, each)

print(maxv)
