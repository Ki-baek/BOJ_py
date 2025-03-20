x = int(input())

start = 64
lst = []

while x != 0:
    if x < start:
        start //= 2
    else:
        x -= start
        lst.append(start)
    
print(len(lst))