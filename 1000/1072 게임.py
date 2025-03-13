x, y = map(int, input().split())

z = y * 100 // x

if z > 98:
    print(-1)

else:
    left = 0
    right = x
    cnt = x

    while left <= right:
        mid = (left + right) // 2
       
        if ((y + mid) * 100) // (x + mid) > z: # 괄호 많이 쏟아질 때는 꼼꼼하게..
            cnt = mid
            right = mid - 1
        else:
            left = mid + 1

    print (cnt)