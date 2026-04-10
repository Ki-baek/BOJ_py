lst = [0] * 16


lst[0] = 2

for i in range(1, 16):
  lst[i] = lst[i - 1] * 2 - 1

n = int(input())

print(lst[n] ** 2)