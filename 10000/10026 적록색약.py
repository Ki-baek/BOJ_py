import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

normal_cnt = 0
cb_cnt = 0

n = int(input().rstrip())
table = [list(input().rstrip()) for i in range(n)]
visited = [[0] * n for i in range(n)]

def dfs(x, y):
  
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  
  for i in range(4):
    a = x + dx[i]
    b = y + dy[i]
    
    if (0 <= a < n) and (0 <= b < n) and table[a][b] == standard and visited[a][b] != 1:
      visited[a][b] = 1
      dfs(a, b)
  
  
  

for i in range(n):
  for j in range(n):
    if visited[i][j] == 0:
      standard = table[i][j]
      dfs(i, j)
      normal_cnt += 1

visited = [[0] * n for i in range(n)]

for i in range(n):
  for j in range(n):
    if table[i][j] == "G":
      table[i][j] = 'R'

for i in range(n):
  for j in range(n):
    if visited[i][j] == 0:
      standard = table[i][j]
      dfs(i, j)
      cb_cnt += 1

print(normal_cnt, cb_cnt)

# https://develop247.tistory.com/248 << 치환 + 재귀를 이용한 코드 내가 생각한 방식이랑 비슷한데 뭔가 다르다..