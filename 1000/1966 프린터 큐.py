from collections import deque

order = deque()

num_of_case = int(input())

for i in range(num_of_case):
    
    count = 0
    n, m = map(int, input().split())
    queue = deque(input().split())
    
    while queue:
        big = max(queue)
        target = queue.popleft()
        m -= 1
        
        if target == big:
            count += 1
            
            if m < 0:
                print (count)
                break
        
        else:
            queue.append(target)
            
            if m < 0:
                m = len(queue) - 1
