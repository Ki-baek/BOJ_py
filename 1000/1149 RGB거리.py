n = int(input())

dp = [[0 for i in range(3)] for _ in range(n + 1)]
num = [[0] * 3]

for i in range(1, n + 1):
  
 
  lst = list(map(int, input().split()))
  num.append(lst)
  
  dp[i][0] = min(dp[i - 1][1] + num[i][0], dp[i - 1][2] + num[i][0])
  dp[i][1] = min(dp[i - 1][0] + num[i][1], dp[i - 1][2]+ num[i][1])
  dp[i][2] = min(dp[i - 1][0] + num[i][2], dp[i - 1][1] + num[i][2])
  
print(min(dp[n][0], dp[n][1], dp[n][2]))

# 어렵네 어려워