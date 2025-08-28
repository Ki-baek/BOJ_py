w, x = map(int, input().split())
y, z = map(int, input().split())

a = w * z + x * y
b = x * z

k = b % a
m = a
n = b
while k != 0:
  b = a
  a = k
  k = b % a
  
lst = [m // a, n // a]

print(*lst)