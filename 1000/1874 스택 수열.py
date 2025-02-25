import sys
input = sys.stdin.readline

from collections import deque

n = int(input().strip())

seq = [int(input()) for i in range(n)]

stack = []

progress = deque()

while seq or stack:

    k = seq.pop()
    stack.append(k)
    progress.appendleft('-')


    while stack and stack[-1] == n:
        stack.pop()
        progress.appendleft('+')
        n -= 1

    if stack and seq and stack[-1] > seq[-1]:
        print('NO')
        sys.exit()


print('\n'.join(progress))
