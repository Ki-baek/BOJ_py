import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, visited, start):

    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    queue = deque(start)

    while queue:
        
        x, y, z = queue.popleft()
        
        for i in range(6):

            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < j and visited[nz][ny][nx] == -1 and graph[nz][ny][nx] != -1:
                visited[nz][ny][nx] = 0
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append((nx, ny, nz))


m, n, j = map(int, input().strip().split())

result = 0
start = []

graph = [[[0] * m for col in range(n)] for depth in range(j)]

visited = [[[-1] * m for col in range(n)] for depth in range(j)]

for i in range(j):
    graph[i] = [list(map(int, input().strip().split())) for k in range(n)]

for i in range(j):
    for k in range(n):
        for l in range(m):
            if graph[i][k][l] == 1 and visited[i][k][l] == -1:
                visited[i][k][l] = 0
                start.append((l, k, i))
                
bfs(graph, visited, start)


for i in graph:
    for k in i:
        for l in k:
            if l == 0:
                print(-1)
                sys.exit()
        result = max(result, max(k))

print(result - 1)


# 그래프에 이게 몇번째인지 기록하면서 하면 cnt같은 귀찮은 변수 안 만들어도 된다
# 1의 위치를 담아주고 시작해야 중복 안된다