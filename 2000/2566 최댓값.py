arr = []

for i in range(9):
  arr.append(list(map(int, input().split())))

max_value = 0
a = 0
b = 0

for i in range(9):
  for j in range(9):
    if max_value < arr[i][j]:
      max_value = arr[i][j]
      a = i
      b = j
    
print(max_value)
print(a + 1, b + 1)