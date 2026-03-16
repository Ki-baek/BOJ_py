n = int(input())

num_lst = list(map(int, input().split()))

result = [num_lst[0]]

for i in range(1, n):
    
    if num_lst[i] <= result[-1]:
        for j in range(len(result)):
            if result[j] >= num_lst[i]:
                result[j] = num_lst[i]
                break
            else:
                continue
    else:
            result.append(num_lst[i])
       
    
print(len(result))


# 진짜 존나 어렵네요
# 이진 탐색이 단순히 중간지점 찍고 어쩌구 하는게 아니고
# 위에 문제처럼 길이만 요구하는 문제에서는 실제 배열의 모습 같은 것은 별로 중요하지 않다는 생각도 해야함