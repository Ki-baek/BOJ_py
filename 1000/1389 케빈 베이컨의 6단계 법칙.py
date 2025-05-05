import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, graph):
    visited = deque()
    queue = deque()
    next = deque()
    cnt = 1
    result = 0
    queue.append(start)

    while queue:
        n = queue.popleft()

        if n not in visited:
            visited.append(n)
            next.extend(sorted(graph[n]))
            result += cnt
        
        if len(queue) == 0:
            queue.extend(next)
            cnt += 1
            next.clear()
    return result

    

N, M = map(int, input().strip().split())

links = {i : [] for i in range(1, N + 1)}
min_KV = N ** 2

for i in range(M):
    a, b = map(int, input().strip().split())
    links[a].append(b)
    links[b].append(a)

for i in range(1, N + 1):
    k = bfs(i, links)
    if k >= min_KV:
        continue
    else:
        min_KV = k
        KV = i

print(KV)