word = list(input())
lis = []
for i in word:
    k = ord(i)
    if k < 68:
        k += 23
    else:
        k -= 3
    
    lis.append(chr(k))

print(''.join(map(str, lis)))