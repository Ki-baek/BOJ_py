n = int(input())
lis1 = []
num1 = set(map(int, input().split()))


m = int(input())
lis2 = []
num2 = list(map(int, input().split()))



for i in num2:
    if i not in num1:
        print(0)
    else:
        print(1)
