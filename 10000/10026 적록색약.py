import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = input().rstrip()
table = [list(input().rstrip()) for i in range(n)]
visited = [[0] * n for i in range(n)]

# https://develop247.tistory.com/248 << 치환 + 재귀를 이용한 코드 내가 생각한 방식이랑 비슷한데 뭔가 다르다..