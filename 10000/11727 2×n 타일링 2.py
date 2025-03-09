n = int(input())

lst = [0] * 1001
lst[1] = 1
lst[2] = 3
for i in range(3, n + 1):
    lst[i] = lst[i - 1] + 2 * (lst[i - 2])

print(lst[n] % 10007)


'''
1 = 1
2 = 3
3 = 5 
4 = 11
5 = 
'''