import sys
input = sys.stdin.readline

n, m = map(int,input().rstrip().split())
matrix_sum = [[0 for i in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
  row_sum = [0] * (n + 1)
  row = list(map(int, input().rstrip().split()))

  for j in range(1, n + 1):
    row_sum[j] = row_sum[j - 1] + row[j - 1]
  
  matrix_sum[i] = [a + b for a, b in zip(matrix_sum[i - 1], row_sum)]



for _ in range(m):
  
  x1, y1, x2, y2 = map(int, input().rstrip().split())
  
  print(matrix_sum[x2][y2] - matrix_sum[x1 - 1][y2] - matrix_sum[x2][y1 - 1] + matrix_sum[x1 - 1][y1 - 1])