from collections import deque

n, b = map(int, input().split())

result = deque()

while n >= b:
    if n % b < 10:
        result.appendleft(str(n % b))
    else:
        result.appendleft(chr(n % b - 10 + ord('A')))
    n //= b

if n < 10:
    result.appendleft(str(n))
else:
    result.appendleft(chr(n % b - 10 + ord('A')))

print(''.join(result))

#____________________맞긴 했는데 뭔가 비효율적인 느낌...?_________________________




# LIST에 미리 1~Z를 저장해 둔 후 나머지 결과에 따라
# 필요한 값을 뽑아쓰는 방법도 있음... 코드 참 신기하네