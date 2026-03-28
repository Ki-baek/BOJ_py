import sys
from collections import deque
input = sys.stdin.readline

com_num = int(input())
com_pair = int(input())
links = {i: [] for i in range(1, com_num + 1)}

def dfs(graph, start):
    visited = set()
    lst = deque()
    
    lst.append(start)
    
    while lst:
        n = lst.pop()
        
        if n not in visited:
            visited.add(n)
            lst.extend(graph[n])
    return len(visited) - 1

for i in range(com_pair):
    a, b = map(int, input().split())
    links[a].append(b)
    links[b].append(a)
    
print(dfs(links, 1))