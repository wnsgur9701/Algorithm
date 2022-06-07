import sys

input = sys.stdin.readline

N = int(input())
target_list = list(map(int, input().split()))

M = int(input())
nums = list(map(int, input().split()))

def binary_search(data, x):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if x == data[mid]:
            return 1
        elif x > data[mid]:
            start = mid + 1
        else:
            end = mid -1
    return 0

target_list.sort()
for num in nums:
    print(binary_search(target_list, num))