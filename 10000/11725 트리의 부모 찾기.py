#BFS

from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())

graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
  a, b = map(int, input().rstrip().split())
  graph[a].append(b)
  graph[b].append(a)
  
visited = [0] * (n + 1)

def bfs(graph, node):
  stack = deque([node])
  while stack:
    parents_node = stack.popleft()
    
    for i in graph[parents_node]:
      if visited[i] == 0:
        visited[i] = parents_node
        stack.append(i)
  return visited
        
bfs(graph, 1)

result = visited[2:]

for i in result:
  print(i)


# DFS
  
import sys
input = sys.stdin.readline

n = int(input().rstrip())

graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
  a, b = map(int, input().rstrip().split())
  
  graph[a].append(b)
  graph[b].append(a)

visited = [0] * (n + 1)

def dfs(graph, node):
  
  stack = [node]
  while stack: 
    parents_node = stack.pop()
    for i in graph[parents_node]:
      if visited[i] == 0:
        visited[i] = parents_node
        stack.append(i)
  
  return visited

dfs(graph, 1)

for k in range(2, n + 1):
  print(visited[k])