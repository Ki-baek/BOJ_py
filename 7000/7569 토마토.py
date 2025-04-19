import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, visited, start):

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    queue = deque(start)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == -1 and graph[x][y] == 1:
                visited[nx][ny] = 0
                queue.append(nx, ny)
                cnt += 1
    
    return cnt

m, n, j = map(int, input().strip().split()) #갑자기 뇌정지 h가 들어가면 코드 어캐짜야하지?