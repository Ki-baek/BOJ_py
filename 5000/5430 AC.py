import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())

for i in range(t):

    reverse = False
    judge = True
    queue = deque(input().rstrip())

    n = int(input().rstrip())

    if n == 0:
        dump = input()
        array = deque()

    else:
        array = deque(map(int, input().strip().strip('[]').split(',')))# strip()를 먼저 붙여서 공백 없애기...


    while queue:

        comm = queue.popleft()
        
        if len(array) == 0:
            if comm == 'D':
                print('error')
                judge = False
                break
        
        else:
            if comm == 'R':
                reverse = not reverse# ★deque.reverse()의 시간 복잡도가 O(n)이라 복잡한 케이스에 오래 걸리니 지표 같은거 하나 만들어서 시간 복잡도를 낮추는 기막힌 아이디어★
            else:
                if reverse:
                    array.pop()
                else:
                    array.popleft()

    if judge:
        if reverse:
            array.reverse()

        lst = []

        for i in array:# 상당히 귀찮은
            lst.append(str(i))# 하지만 알아두긴 해야하나

        print("[" + ",".join(lst) + "]")# 아무튼 입력 바꾸는 과정