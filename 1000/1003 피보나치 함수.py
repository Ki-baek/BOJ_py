import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, b = 1, 0
    
    k = int(input())
    
    for i in range(k):
        a, b = b, b + a
    
    print(a, b)
