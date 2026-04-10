import heapq

T = int(input())

for t in range(T):
  
  n = int(input())
  max_heap = []
  min_heap = []
  cnt = 

  for i in range(n):
    com, op = input().split()
    
    if com == 'I':
      
      val = int(op)
      heapq.heappush(max_heap, val)
      heapq.heappush(min_heap, -val)
      
      
  #     if int(op) >= 0:
  #       queue.append(int(op))
        
  #     else:
  #       heapq.heappush(min_queue, -(int(op)))
      
  #   else:
      
  #     if not queue:
  #       pass
      
  #     elif op == '1':
  #       heapq.heappop(queue)
        
  #     elif op == '-1':
  #       heapq.heappop(min_queue)
  
  # if queue:
  #   print(max(queue), -(max(min_queue)))
    
  # else:
  #   print("EMPTY")