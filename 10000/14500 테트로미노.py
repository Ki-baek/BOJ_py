import sys
input = sys.stdin.readline

def tetromino(x, y):
  
  
  
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  
  for i in range(4):
    now_x, now_y = x + dx[i], y +dy[i]
    
      


lst = []
n, m = map(int, input().rsplit())

lst = [list(map(int, input().rstrip().split())) for _ in range(n)]

