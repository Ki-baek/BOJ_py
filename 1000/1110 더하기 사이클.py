n = int(input())

k = n
count = 0

while 1:
    result = 0
    nums = list(str(k))

    for i in nums:
        result += int(i)

    re_lst = list(str(result))

    k = int(nums[-1] + re_lst[-1])
    count += 1

    if k == n:
        break

print(count)