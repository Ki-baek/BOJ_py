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


# https://velog.io/@lucky-korma/DFS-BFS%EC%9D%98-%EC%84%A4%EB%AA%85-%EC%B0%A8%EC%9D%B4%EC%A0%90
# 정점마다의 특징을 저장하면서 가야할 때(같은 경로 內 같은 숫자가 있으면 안된다는 조건 등) -> DFS, BFS는 경로 내 특징을 저장하며 가기에는 많이 비효율?적인 듯
# 최단 거리를 구해야할 때 -> BFS, 시작점에서 가까운 곳 부터 찾으며 가기 때문에 최단 거리를 구하기 더 용이하다