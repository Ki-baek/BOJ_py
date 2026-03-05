n, m = map(int, input().split())

result = m * n

if result % 2 == 1:
  print(result - 1)
  
else:
  print(result)