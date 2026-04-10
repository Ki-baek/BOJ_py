import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

h = list(map(int, input().rstrip().split()))

a = list(map(int, input().rstrip().split()))

print(max(h) + max(a))