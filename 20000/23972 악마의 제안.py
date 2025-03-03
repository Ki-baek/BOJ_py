# (m - k) * n = m
# m // n = (m - k)
#1 // n = 1 - k//m
#1 // n -1 = - k // m
# 1 - 1 // n = k // m
# n - 1 // n = k // m
# m(n - 1) = k * n 
# m = k * n // n - 1
import sys

k, n = map(int, input().split())
if n == 1:
    print(-1)
    sys.exit()
m = (k * n) // (n - 1)
if (k * n) % (n - 1):
    m += 1
print(m)