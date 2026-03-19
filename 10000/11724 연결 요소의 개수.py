import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

dots = {i: [] for i in range(1, N + 1)}

def dfs(graph, nums):
    
    not_visited = list(range(1, nums + 1))
    queue = deque()
    count = 0
    
    while not_visited:
        a = not_visited.pop()
        not_visited.append(a)
        queue.append(a)
        
        while queue:
            
            k = queue.pop()
            
            if k in not_visited:
                
                not_visited.remove(k)
                queue.extend(graph[k])
                
        count += 1
        
    return count
    

for i in range(M):
    u, v = map(int, input().split())
    dots[u].append(v)
    dots[v].append(u)

print(dfs(dots, N))