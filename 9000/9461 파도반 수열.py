# 1 1 1 2 2 3 4 5 7 9 12 16 21

# n - 5 + n - 1 = n
import sys
input = sys.stdin.readline

t = int(input().strip())


for i in range(t):
    n = int(input().strip())
    pn = [1, 1, 1, 2, 2]
    pn.extend([0] * (n - 3))

    for i in range(5, n + 1):
        pn[i] = pn[i - 5] + pn[i - 1] # 점화식 i - 5, 5이하 값은 미리 생성(1929 아이디어)
    print(pn[n - 1])