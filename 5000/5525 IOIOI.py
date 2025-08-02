n = int(input())
m = int(input())

S = input()

Pn = 'I' + 'OI' * n

i = 0
cnt = 0
result = 0

while i < (m - 1):

    if S[i : (i + 3)] == 'IOI':
        cnt += 1
        i += 2

        if cnt == n:
            cnt -= 1
            result += 1

    else:
        i += 1
        cnt = 0

print(result)


# 아이디어가 지리는 문제
# https://yiyj1030.tistory.com/495 KMP알고리즘에대한설명
# 사실 슬라이싱이랑 아이디어만 있으면 풀리는.. KMP 왜 파고있었지
# https://www.acmicpc.net/board/view/149444 그렇다니까 일단 다른 알고리즘 습득하는데 집중