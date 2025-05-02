from collections import deque

def dfs():
    for i in range(n):
        

n = int(input())

array = deque(map(int, input().split()))

lst = []

lst.append(array.popleft())
