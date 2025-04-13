import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, visited, start):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([start])

    visited[start[0]][start[1]] = 0 # 출발점 방문한 걸로 표시

    while queue: # 탐색 시작~!
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and graph[nx][ny] == 1: # 등호 하나가 코드 전체를 박살낼 수 있다..
                visited[nx][ny] = visited[x][y] + 1 # 현재 노드 까지의 최단 거리 + 1 = 다음 노드까지 최단 거리
                queue.append((nx, ny)) 

n, m = map(int, input().strip().split()) # m , n 입력받기

graph = [[0] * m for i in range(n)] # 빈 그래프 그리기

visited = [[-1] * m for j in range(n)] # 방문하지 않은 노드를 -1로 초기화

for i in range(n):
    graph[i] = list(map(int, input().strip().split())) # 그래프 입력받기

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start = (i, j)
        elif graph[i][j] == 0:
            visited[i][j] = 0 # 갈 수 없는 노드를 0으로 설정

bfs(graph, visited, start)

for i in range(n):
    for j in range(m):
        print(visited[i][j], end = ' ')
    print('')