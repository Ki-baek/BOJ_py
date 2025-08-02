from collections import deque
import sys

ISBN = deque(list(input()))

result = 0
judge = False

for i in range(6):
    
    k = ISBN.popleft()

    if k != '*':
        result += int(k)
    
    k = ISBN.popleft()

    if k != '*':
        result += 3 * (int(k))
    else:
        judge = True

k = ISBN.popleft()

if k != '*':
    result += int(k)

if judge:

    for j in range(1,10):

        if ((3 * j) + result) % 10 == 0:
            print(j)
            sys.exit()

    print(0)


else:

    m = 10 - (result % 10)

    if m == 10:
        print(0)
    else:
        print(m)