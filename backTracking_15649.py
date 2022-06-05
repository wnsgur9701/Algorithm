"""
1. 아이디어
- 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택(이때 방문여부 확인)
- 재귀함수에서 M개를 선택한 경우 print

2. 시간 복잡도 (2억이 넘지 말아야 한다)
N * N : 중복이 가능, N = 8 까지 가능
N! : 중복이 불가, N = 10 까지 가능

3. 자료구조
방문 여부 확인 배열 : bool[]
선택한 값 입력 배열: int[]

팁
- 백트래킹 문제는 n이 작음
- 재귀함수 사용할 때, 종료 시점 잊지 말기!
"""





import sys

input = sys.stdin.readline

n, m = map(int, input().split())
rs = []
# 인덱스에 바로 가기 위해서 n + 1
check = [False] * (n+1)

def recur(num):
    if num == m:
        print(' '.join(map(str, rs)))
    for i in range(1, n+1):
        if check[i] == False:
            check[i] == True
            rs.append(i)
            recur(num+1)
            check[i] == False
            rs.pop()

recur(0)