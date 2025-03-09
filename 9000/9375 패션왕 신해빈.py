import sys
input = sys.stdin.readline

def fashion_king(a):
    
    visited = {}

    for i in range(a):
        clothes, type = map(str, input().split())
        if type not in visited:
            visited[type] = 1
        
        else:
            visited[type] += 1
    
    return visited.values()

def ways(array):
    result = 1
    while array:
        result *= (array.pop() + 1)
    return (result - 1)


t = int(input().strip())




for i in range(t):
    n = int(input().strip())
    clothes_num = list(fashion_king(n))
    print(ways(clothes_num))