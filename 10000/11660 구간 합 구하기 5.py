import sys
input = sys.stdin.readline

n, m = map(int,input().rstrip().split())
preSum_matrix = [[[0] for _ in range(n)] for _ in range(n)]

for i in range(n):
  row = list(map(int, input().rstrip().split()))
  

for i in range(m):
  x1, y1, x2, y2 = map(int, input().rstrtip().split())
  