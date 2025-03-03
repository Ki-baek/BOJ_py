n = int(input())

names = [input() for i in range(n)]

for i in names:
    if 'S' in i:
        print(i)
        break