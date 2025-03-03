lst = []

while 1:
    k = input()

    if k == '=':
        break

    elif k.isnumeric():
        k = int(k)
        lst.append(k)

    elif k == '+':
        h = int(input())
        k = lst.pop()
        lst.append(k + h)

    elif k == '-':
        h = int(input())
        k = lst.pop()
        lst.append(k - h)

    elif k == '*':
        h = int(input())
        k = lst.pop()
        lst.append(k * h)

    elif k == '/':
        h = int(input())
        k = lst.pop()
        lst.append(k // h)

print(lst.pop())