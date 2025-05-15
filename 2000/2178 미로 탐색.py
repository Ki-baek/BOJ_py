from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

def bfs(a, b):

    queue = deque([(a, b)])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:

        x, y = queue.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m: # 이걸 m이 아니라 y라고 적는 바람에 ....

                if graph[nx][ny] == 1:

                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
    
    return graph[n - 1][m - 1]

print(bfs(0, 0))

# 최단 거리 구할땐 BFS, G 자체에 그 칸까지 이동하는 횟수 적으면서 가는 아이디어