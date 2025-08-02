def arr_swap(a, b):
  while a < b:
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    a += 1
    b -= 1
    
n, m = map(int, input().split())

arr = list(range(1, n + 1))
  
for i in range(m):
  i, j = map(int, input().split())
  
  arr_swap(i - 1, j - 1)

print(*arr)