n = int(input())

count = 0
target_num = 666

while 1:
    if '666' in str(target_num):
        count += 1

    if count == n:
        break

    target_num += 1

print(target_num)
