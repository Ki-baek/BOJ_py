import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, visited, start):

    count = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque([start])

    visited[start[0]][start[1]] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and graph[nx][ny] == '1':
                visited[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    return count            

n = int(input().strip())


graph = [list(input().strip()) for i in range(n)]
cnt = 0
result = []
visited = [[-1] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and visited[i][j] == -1:
            cnt += 1
            start = (i, j)
            result.append(bfs(graph, visited, start))

result.sort()

print(cnt)
for i in result:
    print(i)