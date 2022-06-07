"""
1. 아이디어
- N개의 숫자를 정렬
- N개를 for 돌면서, 이진탐색
- 이진탐색 안에서 마지막에 데이터 찾으면, 1출력, 아니면 0 출력

2. 시간 복잡도
- N개 입력값 정렬 = O(NlogN)
- M개를 N개 중에서 탐색 = O(M*logN)
- 총합 : O((N+M)logN) > 가능

3. 자료구조
- N개 숫자 : int[]
- M개 숫자 : int[]
"""






import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
target_nums = list(map(int, input().split()))

# 이진 정렬을 하기 위해서는 먼저 정렬을 해야한다. 그래야지 이진 탐색을 통해 걸러낼 수 있으니까
nums.sort()

def bi_search(start, end, target):

    if start == end:
        if nums[start] == target:
            print(1)
        else:
            print(0)
        # print를 한 후에 종료를 해야하니 return을 해준다
        return

    mid = (start + end)//2

    if nums[mid] < target:
        bi_search(mid+1, end, target)
    else:
        bi_search(start, mid, target)

for each in target_nums:
    # 0번째 인덱스부터 N-1번째 인덱스 까지 확인을 해야한다.
    bi_search(0,N-1, each)

