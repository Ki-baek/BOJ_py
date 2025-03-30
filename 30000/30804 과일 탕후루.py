# deque로 하나하나 pop해서 하는게 아닌
# 리스트 슬라이싱으로 구현하는 것도 아닌
# dict이용해서 구현했어야한다
# 투포인터라는 개념이 나한테는 생소한데 문제가 참 많이나와있다
# https://dongdongfather.tistory.com/69 << defaultdict 설명 유?사 딕셔너리 란다#
# https://m.blog.naver.com/kks227/220795165570 << 투 포인터 관련글
n = int(input())

huru = list(map(int, input().split()))

start, end = 0, len(huru) - 1

while 1:
    if len(set(huru[start:end + 1])) > 2:
        if start <= end - 1:
            end -= 1
        if start + 1 <= end:
            start += 1
    else:
        if len(set(huru[start - 1: end + 1])) <= 2 and start > 0:
            start -= 1
        elif len(set(huru[start:end])) <= 2:
            end += 1
            if end >= len(huru):
                end -= 1
        break

print(end - start + 1)
