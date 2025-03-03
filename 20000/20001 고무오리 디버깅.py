dump = input()

pro = 0

while 1:
    string = input()
    if string == '문제':
        pro += 1
    elif string == '고무오리':
        if pro == 0:
            pro += 2
        else:
            pro -= 1
    elif string == '고무오리 디버깅 끝':
        break

if pro == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')