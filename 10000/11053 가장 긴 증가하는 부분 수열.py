n = int(input())

num_lst = list(map(int, input().split()))

max_len = [1]
max_num = [num_lst[0]]

for i in range(1, n):
    for j in range(len(max_num)):
        if max_num[j] > num_lst[i]:
            max_num.append(num_lst[i])
            max_len.append(1)
        elif max_num[j] < num_lst[i]:
            max_num[j] = num_lst[i]
            max_len[j] += 1
        else:
            continue

print(max(max_len))