# 시간 초과 때문에 pypy3으로 제출해야함(이중 반복문)

import sys

input = sys.stdin.readline

def flat():
    global height
    
    block = B

    for i in ground:
        if i <= g:
            time[g] += g - i
            block -= g - i
        
        else:
            time[g] += 2 * (i - g)
            block += i - g

    if block >= 0 and time[g] <= time[height]:
        height = g

N, M, B = map(int, input().strip().split())
ground = []

for i in range(N):
    ground.extend(map(int, input().split()))

time = [0] * 257

height = 0

for g in range(257):

    flat()
    
    
print(time[height], height)

# https://www.acmicpc.net/board/view/138638 반례 모음집