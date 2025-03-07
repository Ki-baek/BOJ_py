import sys
input = sys.stdin.readline

n = int(input().strip())
count = 0

if n >= 100:
    count += 99
    for i in range(100, n + 1):
        lst = list(str(i))
        if int(lst[0]) + int(lst[2]) == 2 * int(lst[1]):
            count += 1
else:
    count += n

print(count)