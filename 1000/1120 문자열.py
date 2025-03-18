a, b = input().split()

result = []

for i in range(len(b)- len(a) + 1):

    count = 0

    for j in range(len(a)):

        if a[j] != b[j + i]:
            count += 1

    result.append(count)

print(min(result))

# 아니 이걸 어떻게 브루트포스로 짤 생각을 하지? 발상 좀 배워가기