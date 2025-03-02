import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

k, n = map(int, input().split())

lans_i_own = [int(input().strip()) for i in range(k)]

longest_lan = max(lans_i_own)

def searching(low, high):
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

searching(0, longest_lan)
print(max_lan)