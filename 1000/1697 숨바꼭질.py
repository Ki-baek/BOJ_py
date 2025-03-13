from collections import deque

def search():
    queue = deque()

    queue.append(n)

    while queue:
        a = queue.popleft()

        if a == k:
            print(visited[a])
            break
        
        for i in (a - 1, a + 1, a * 2):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[a] + 1
                queue.append(i) 

n, k = map(int, input().split())

limit = 100000

visited = [0] * (limit + 1)

search()

# 이해는 되는데 구현이 어렵네