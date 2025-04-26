import sys
input = sys.stdin.readline

T = int(input().strip())

for i in range(T):
    i, j = 1, 1
    cnt = 1
    M, N, x, y = map(int, input().strip().split())

    while (i != x and j != y) or (i != M and j != N):
        if i < M:
            i += 1
        else:
            i = 1

        if j < N:
            j += 1
        else:
            j = 1
        cnt += 1
    
    print(cnt)