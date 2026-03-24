import sys

c, r = map(int, input().split())

k = int(input())

if c * r < k:
  print(0)
  sys.exit()
  

  
cnt = 0
col = 1
row = 0


while True:
  
  
  for i in range(r):
    cnt += 1
    row += 1

    if cnt == k:
      print(f'{col} {row}')
      sys.exit()

  c -= 1

  for i in range(c):
    cnt += 1
    col += 1
    
    if cnt == k:
      print(f'{col} {row}')
      sys.exit()
  
  r -= 1
      
  for i in range(r):
    cnt += 1
    row -= 1
    
    if cnt == k:
      print(f'{col} {row}')
      sys.exit() 
      
  c -= 1
  
  for i in range(c):
    cnt += 1
    col -= 1
    
    if cnt == k:
      print(f'{col} {row}')
      sys.exit()
      
  r -= 1