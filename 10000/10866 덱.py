import sys
input = sys.stdin.readline

from collections import deque

n = int(input().strip())

lst = deque()

for i in range(n):
    command = input().split()

    if command[0] == 'push_back':
        lst.append(command[1])

    elif command[0] == 'push_front':
        lst.appendleft(command[1])

    elif command[0] == 'pop_front':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.popleft())

    elif command[0] == 'pop_back':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop())

    elif command[0] == 'size':
        print(len(lst))

    elif command[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'front':
        if len(lst) == 0:
            print(-1)
        else:
            k = lst.popleft()
            print(k)
            lst.appendleft(k)

    elif command[0] == 'back':
        if len(lst) == 0:
            print(-1)
        else:
            k = lst.pop()
            print(k)
            lst.append(k)