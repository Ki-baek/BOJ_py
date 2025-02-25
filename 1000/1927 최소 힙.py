import heapq
import sys
input = sys.stdin.readline

n = int(input().strip())
stack = []
heapq.heapify(stack)

for i in range(n):
    
    num = int(input().strip())
    
    if num == 0:
        if len(stack) == 0:
            print(0)
        else:
            print(heapq.heappop(stack))
    else:
        heapq.heappush(stack, num)
