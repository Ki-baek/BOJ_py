import sys
input = sys.stdin.readline

n = int(input().strip())

lst = list(map(int, input().strip().split()))

lst_set = sorted(list(set(lst)))
dic = {}

for i in range(len(lst_set)):
    dic[lst_set[i]] = i #dic key == lst elements, dic value == "X prime(in question)"

for i in lst:
    print(dic[i], end = ' ') # getting "X primes" by calling lst elements as dic key