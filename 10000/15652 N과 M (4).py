n, m = map(int, input().split())

lst = []

def dfs(i):
    if len(lst) == m:
        print(*lst)
        return
    
    for j in range(i, n + 1):
        lst.append(j)
        dfs(j)
        lst.pop()
        
dfs(1)