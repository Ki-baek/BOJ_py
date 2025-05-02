def dfs():
    if len(lst) == m:
        print (' '.join(map(str, lst)))

    for i in range(n):

        if visited[i] == 0:

            visited[i] += 1
            lst.append(array[i])
            dfs()
            lst.pop()
            visited[i] -= 1

n, m = map(int, input().split())

array = list(map(int, input().split()))

lst = []

visited = [0] * (n + 1)

array.sort()

dfs()