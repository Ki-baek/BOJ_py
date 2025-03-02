import sys
input = sys.stdin.readline

k, n = map(int, input().split())

lans_i_own = [int(input().strip()) for i in range(k)]

longest_lan = max(lans_i_own)

def searching(low, high):
    if low > high:
        return#이거 유무가 recursion error 생기게 할줄 몰랐지..
    
    global n
    global max_lan

    mid = (low + high) // 2
    count = 0

    for i in lans_i_own:
        count += i // mid
    
    if count >= n:
        max_lan = mid
        searching(mid + 1, high)
    
    else:
        searching(low, mid - 1)

searching(1, longest_lan)#ZeroDivisionError, low 초기값 0이 아니라 1
print(max_lan)

#결국은 처음 생각한게 맞았으니까 자신감있게 밀고 나가고, 진짜 생각이 안날때 도움받기