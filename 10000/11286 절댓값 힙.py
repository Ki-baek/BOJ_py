import heapq
import sys
input = sys.stdin.readline

heap = []
n = int(input())

for i in range(n):
  num = int(input())
  
  if num != 0:
    heapq.heappush(heap, (abs(num), num))
    
  else:
    if len(heap) ==0:
      print(0)
    else:
      item = heapq.heappop(heap)[1]
      print(item)