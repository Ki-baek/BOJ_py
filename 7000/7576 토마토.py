#dfs로 가면 시간 초과가 날 수 밖에 없어.......bfs로

import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().strip().split())

box = [list(map(int, input().strip().split())) for i in range(n)]

queue = deque()

for a in range(n):
    for b in range(m):
        if box[a][b] == 1:
            queue.append([a, b])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < m) and box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1
            queue.append([nx, ny])

result = 0

for line in box:
    for tomato in line:
        if tomato == 0:
            print(-1)
            sys.exit()
    result = max(result, max(line))

print(result - 1)