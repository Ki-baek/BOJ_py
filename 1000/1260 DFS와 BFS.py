import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int,input().split())

links = {i : [] for i in range(1, n + 1)}

def dfs(graph, start):
    visited = deque()
    lst = deque()
    
    lst.append(start)
    
    while lst:
        n = lst.popleft()
        
        if n not in visited:
            visited.append(n)
            lst.extendleft(reversed(sorted(graph[n])))
    
    return visited

def bfs(graph, start):
    visited = deque()
    lst = deque()
    
    lst.append(start)
    
    while lst:
        n = lst.popleft()
        
        if n not in visited:
            visited.append(n)
            lst.extend(sorted(graph[n]))
    
    return visited
    
for i in range(m):
    a, b = map(int, input().split())
    links[a].append(b)
    links[b].append(a)

print(*(dfs(links, v)))
print(*(bfs(links, v)))
