import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, visited, start):

    global cnt
    

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque([start])

    visited[start[0]][start[1]] = cnt

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and int(graph[nx][ny]) == 1:
                visited[nx][ny] = cnt
                queue.append((nx, ny))

    cnt += 1            

n = int(input().strip())


graph = [[0] * n for i in range(n)]
cnt = 1

visited = [[-1] * n for i in range(n)]

for i in range(n):
    graph[i] = list(input().strip())

for i in range(n):
    for j in range(n):
        if int(graph[i][j]) == 1:
            start = (i, j)
            bfs(graph, visited, start)

print(cnt - 1)
for i in range(cnt - 1):
    print(visited.count(i))