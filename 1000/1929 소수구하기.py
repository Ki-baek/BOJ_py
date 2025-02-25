m, n = map(int, input().split())

arr = [0] * (n + 1)
arr[0] = 1
arr[1] = 1

for i in range(2, n + 1):
  if arr[i] == 0:
    j = 2
    while i * j <= n:
      arr[i * j] = 1
      j += 1

for i in range(m, n + 1):
  if arr[i] == 0:
    print(i)
