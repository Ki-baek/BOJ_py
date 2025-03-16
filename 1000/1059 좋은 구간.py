l = int(input())

s = list(map(int, input().split()))
s.sort()

n = int(input())

if n in s or s[-1] < n:
    print(0)

else:
    
    for i in range(l):

        k = s.pop()

        if k > n:
            big = k
        
        else:
            small = k
            break
    if not('small' in globals()):
        small = 0

    start = small + 1
    end = big - 1
    result = 0

    for i in range(start, n):
        result += end - n + 1
    
    result += end - n

    print(result)
    # 자 봐봐 시작점이 정해져썽
    # 스타트가 34부터야 34부터 99까지인데 
    # 34~ 58까지는 안세잖아 59가 안들어가니까
    # 그럼 99 - 58을 하면 딱 41 나오네
    # 그럼 그렇게 35 ~ 58 그럼 이제 그렇게하다가 59가 맨 앞에오는 상황에서는? 99 -60 즉 40개를 더해줘야한다 
    # 그럼 34~58이 앞에 총 25회 온다
    # 34~ 58 즉 25이다