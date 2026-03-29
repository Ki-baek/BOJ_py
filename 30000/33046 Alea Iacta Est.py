A, B = map(int, input().split())

C, D = map(int, input().split())

sum1 = (A + B) % 4

if sum1 == 0:
  sum1 = 4

sum2 = (C + D) % 4

if sum2 == 0:
  sum2 = 4

sum2 -= 1

result = (sum1 + sum2) % 4

if result == 0:
  result = 4

print(result)