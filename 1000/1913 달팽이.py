# 반드시 벡터 쓰는거에 익숙해지자,,,
n = int(input())

k = int(input())

x, y = n // 2, n // 2

lst = [[0 for i in range(n)] for _ in range(n)] 

lst[y][x] = 1
target_x, target_y = x, y

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

val = 2
dist = 1
vector = 0

while val <= n ** 2:
  for _ in range(2):
    for _ in range(dist):
      if val > n ** 2:
        break
      
      y += dy[vector]
      x += dx[vector]
      
      lst[y][x] = val
      
      if val == k:
        target_x, target_y = x, y
        
      val += 1
      
    vector = (vector + 1) % 4
    if val > n ** 2:
      break
    
  dist += 1
  

for i in lst:
  print(*i)

print(target_y + 1, target_x + 1)