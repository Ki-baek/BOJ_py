n = int(input())

a = list(map(int, input().split()))

sorted_a = sorted(a)
p = []

for i in range(n):
    p.append(sorted_a.index(a[i]))
    sorted_a[sorted_a.index(a[i])] = 0

print (*p)