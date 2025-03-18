# 1 / 2 3 / 4 5 6 / 7 8 9 10 / 11 12 13 14 15 / 16 17 18 19 20 21 / 22 23 24 25 26 27 28

''' while cnt <= k:
        cnt += i
        i += 1

    
    i가 몇인지 나오고
    k - cnt + 1 = num이라하면
    i + 1이 분모/ 자 더한 값이고
    i % 2를 해서 1 / i부터 시작인지 i / 1 부터 시작인지 결정
    >> 0이면, 즉 false면 i / 1부터고 1, true면 1 / i 부터
    해서 range(1, num)으로 for문 돌려서 분수 찾기!!! a, b 변수 설정

    '''

n = int(input())

cnt = 0
k = 0

while cnt < n:
    k += 1
    cnt += k

locate = cnt - n



if k % 2 == 0:
    a = k
    b = 1
    for i in range(0, locate):
        a -= 1
        b += 1
else:
    a = 1
    b = k
    for i in range(0, locate):
        a += 1
        b -= 1

print(str(a)+ '/' + str(b))