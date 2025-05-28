from math import sqrt

t = int(input())

for i in range(t):

    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if dist == 0 and r1 == r2:
        print(-1)

    elif abs(r1 - r2) == dist or r1 + r2 == dist:
        print(1)

    elif abs(r1 - r2) < dist < (r1 + r2):
        print(2)
    
    else:
        print(0)

# 원의 방정식, 두 원이 내접/외접할때, 두 원이 겹칠때(서로다른두점에서만날때), 동심원을 그릴 때 케이스를 나눠야함
# 이거 고등 수학 문제인가용 기억이 안나서 못풀겠음