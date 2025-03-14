n, m = map(int, input().split())
lst = []

count = 0

for i in range(n):
    lst.append(input())

for i in range(m):
    string = input()
    if string in lst:
        count += 1

print(count)