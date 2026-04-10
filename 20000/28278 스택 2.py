import sys
input = sys.stdin.readline

n = int(input().rstrip())

queue = []

for _ in range(n):
  com = input().rstrip().split()
  
  if com[0] == '1':
    queue.append(com[1])
    
  elif com[0] == '2':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue.pop())
      
  elif com[0] == '3':
    print(len(queue))
    
  elif com[0] == '4':
    if len(queue) == 0:
      print(1)
    else:
      print(0)
  elif com[0] == '5':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[-1])