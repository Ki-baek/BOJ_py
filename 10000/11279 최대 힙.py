import heapq
import sys
input = sys.stdin.readline

n = int(input().strip())

stack = []

for i in range(n):
    x = int(input().strip())

    if x == 0:
        if len(stack) == 0:
            print(0)
        else:
            print(heapq.heappop(stack)[1])
    else:
        heapq.heappush(stack, (-x, x))