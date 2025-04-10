# deque로 하나하나 pop해서 하는게 아닌
# 리스트 슬라이싱으로 구현하는 것도 아닌
# dict이용해서 구현했어야한다
# 투포인터라는 개념이 나한테는 생소한데 문제가 참 많이나와있다
# https://dongdongfather.tistory.com/69 << defaultdict 설명 유?사 딕셔너리 란다#
# https://m.blog.naver.com/kks227/220795165570 << 투 포인터 관련글
import sys
input = sys.stdin.readline

n = int(input())

huru = list(map(int, input().split()))

left = 0
cnt = {}
maxlen = 0

for right in range(n):
    now = huru[right]

    if now in cnt:
        cnt[now] += 1
    else:
        cnt[now] = 1

    while len(cnt) > 2:
        remove = huru[left]

        cnt[remove] -= 1

        if cnt[remove] == 0:
            del cnt[remove]
        
        left += 1

    maxlen = max(maxlen, right - left + 1)

print(maxlen)