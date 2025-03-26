#분할정복 사분면을 계~속 쪼개가며 찾아야됨

n, r, c = map(int, input().split())

size = ((2 ** n) // 2) - 1

if r <= size:
    if c <= size:
        locate = 1
    else:
        locate = 2
else:
    if c <= size:
        locate = 3
    else:
        locate = 4

