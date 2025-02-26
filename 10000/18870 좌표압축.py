import sys
input = sys.stdin.readline()

n = int(input())

x = [int(input().split()) for i in range(n)]

x_prime = [0] * (n + 1)

for i in range(n):
    for j in range(n):
        if x[i] > x[j]:
            x_prime[i] += 1

print(*x_prime)
