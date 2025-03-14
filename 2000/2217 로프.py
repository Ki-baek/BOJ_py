from collections import deque

n = int(input())

rope = [int(input()) for i in range(n)]

rope.sort()
ropes = deque(rope)
result = 0

while ropes:
    k = ropes.popleft()
    result = max(result, k * (len(ropes) + 1))

print(result)