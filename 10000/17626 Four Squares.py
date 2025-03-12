# 0 1 2 3 1 2 3 4 2 1 02 03 04 02 03 04 01 02 02 
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 

# dptable[i - i보다 작은 제곱수] + 1
def FS(a):
    for i in range(2, a + 1):
        mini = 4
        j = 1
        while (j ** 2) <= i:
            mini = min(mini, dp[i - j ** 2])
            j += 1
        dp.append(mini + 1)


n = int(input())
dp = [0, 1]
FS(n)
print(dp[n])