import sys
input = sys.stdin.readline

lis = set()
both = []

n, m = map(int, input().split())

for i in range(n):
    lis.add(input().strip())
for i in range(m):
    saw = input().strip()
    if saw in lis:
        both.append(saw)
        
both.sort()

print(len(both))

for i in both:
    print(i)
