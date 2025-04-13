n = int(input())
sang_card = set(map(int, input().split()))

m = int(input())
card = list(map(int, input().split()))
result = [0] * m

for i in range(m):
    if card[i] in sang_card:
        result[i] += 1

print(*result)