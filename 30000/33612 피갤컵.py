lst = [2024, 8]

n = int(input())

lst[1] += ((n-1) * 7)
lst[0] += lst[1] // 12
lst[1] %= 12
if lst[1] == 0:
  lst[1] = 12
  lst[0] -= 1

print(*lst)