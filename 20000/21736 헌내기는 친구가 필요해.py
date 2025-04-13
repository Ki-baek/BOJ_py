# 일단 DFS/BFS 이용하는 너낌?
# 과연 DFS BFS 중에 어떤게 더 효율적일까
# 어디로 가도 딱히 상관이 없는듯 굳이 재귀로 복잡하게 가지 말고 BFS 쓰자

import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, visited, start):
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([start])
    cnt = 0
    visited[start[0]][start[1]] = 0 # 출발점 방문한 걸로 표시

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and graph[nx][ny] != 'X':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny)) 
                if graph[nx][ny] == 'P':
                    cnt += 1
    
    if cnt == 0:
        return ("TT")
    else:
        return cnt
n, m = map(int, input().strip().split())


graph = [[0] * m for i in range(n)]

visited = [[-1] * m for j in range(n)]

for i in range(n):
    graph[i] = list(input().strip())

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            start = (i, j)
        elif graph[i][j] == 'X':
            visited[i][j] = 0
        else:
            visited[i][j] = -1

print(bfs(graph, visited, start))