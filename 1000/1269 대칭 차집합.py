m, n = map(int, input().split())

x = set(map(int, input().split()))
y = set(map(int, input().split()))

a = x - y
b = y - x

sett = a | b

print(len(sett))