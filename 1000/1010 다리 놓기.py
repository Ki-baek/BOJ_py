def cal_n(a, b):
    if a == 1:
        return b
    
    result = 1

    for i in range(a):
        result *= (b - i)

    return result

def cal_r(a):
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    print(cal_n(n, m) // cal_r(n))