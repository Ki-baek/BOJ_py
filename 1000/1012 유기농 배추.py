import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

def dfs(x, y):
    plus_x = [1, -1, 0, 0]
    plus_y = [0, 0, 1, -1]
    
    for i in range(4):
        check_x = x + plus_x[i]
        check_y = y + plus_y[i]
        
        if (0 <= check_x < row) and (0 <= check_y < col) and field[check_y][check_x] == 1:
            field[check_y][check_x] = 2
            dfs(check_x, check_y)
    
for l in range(t):
    row, col, spot = map(int, input().split())
    field = [[0 for i in range(row)] for j in range(col)]
    
    for k in range(spot):
        m, n = map(int, input().split())
        field[n][m] = 1
    
    count = 0
    for a in range(row):
        for b in range(col):
            if field[b][a] == 1:
                dfs(a, b)
                count += 1
    print(count)
