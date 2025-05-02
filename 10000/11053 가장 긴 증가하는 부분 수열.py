from collections import deque

n = int(input())

array = deque(map(int, input().split()))

lst = []

lst.append(array.popleft())

while array:
    k = array.popleft()
    if k > lst[-1]:
        lst.append(k)

print(len(lst))