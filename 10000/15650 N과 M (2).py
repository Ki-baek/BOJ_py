def dfs():

    if len(lst) == m and sorted(lst) == lst:
        print(' '.join(map(str, lst)))
        return
    
    for i in range(1, n + 1):
        if visited[i] == 0:
            visited[i] = 1
            lst.append(i)
            dfs()
            lst.pop()
            visited[i] = 0
        


n, m = map(int, input().split())

lst = []

visited = [0] * (n + 1)

dfs()