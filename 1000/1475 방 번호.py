num = input()
lst = []

for i in num:
    lst.append(int(i))

cnt = [0] * 9
judge = True

for i in lst:
    if (i == 6 or i == 9) and judge:
        cnt[6] += 1
        judge = False
    elif (i == 6 or i == 9):
        judge = True
    else:
        cnt[i] += 1

print(max(cnt))