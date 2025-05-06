import sys
from collections import deque

input = sys.stdin.readline

N, M, B = map(int, input().strip().split())

result = 0
cnt_h = [0] * 257
blocks = deque()
cnt = 0
adjusted = 0

for i in range(N):
    blocks.extend(list(map(int,input().strip().split())))

for i in blocks:
    cnt_h[i] += 1

standard_h = cnt_h.index(max(cnt_h))

for i in range(len(blocks)):

    k = blocks.pop()

    if k != standard_h:
        k -= standard_h
        blocks.appendleft(k)
    else:
        cnt += 1

required_b = sum(blocks)

if required_b >= 0:

    n = blocks.pop()

    if n > 0:
        result += n * 2
    else:
        result += n * (-1)

elif -(required_b) > B:

    while -(required_b) >= B:

        B += cnt
        result += cnt * 2
        standard_h -= 1
        adjusted += 1


    n = blocks.pop()
    n += adjusted

    if n > 0:
        result += n * 2
    else:
        result += n * (-1)

else:
    n = blocks.pop()

    if n > 0:
        result += n * 2
    else:
        result += n * (-1)

print(result, standard_h)

# https://www.acmicpc.net/board/view/138638