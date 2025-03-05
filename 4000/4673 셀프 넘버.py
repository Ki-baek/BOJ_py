def non_selfnum(n):
    lst = list(str(n))
    result = 0
    for i in lst:
        result += int(i)
    result += n
    return result

selfnum = set()
for i in range(10000):
    selfnum.add(non_selfnum(i))
for i in range(10000):
    if i not in selfnum:
        print(i)