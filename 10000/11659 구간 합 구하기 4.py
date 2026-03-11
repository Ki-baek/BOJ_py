import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums_sum = [0] * (n + 1)

for i in range(1, n + 1):
    nums_sum[i] = nums_sum[i - 1] + nums[i - 1]
    
for k in range(m):
    i, j = map(int, input().split())
    print(nums_sum[j] - nums_sum[i - 1])