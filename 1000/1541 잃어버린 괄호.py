# + 끼리 먼저 묶어서 처리 >> 제일 낮은값?
import sys
input = sys.stdin.readline

exp = list(input().strip().split('-'))

judge = 0
result = 0

if len(exp) == 1:
    nums = list(exp[0].split('+'))
    for i in nums:
        result += int(i)
    print(result)

else:
    if '+' in exp[0]:
        nums = list(exp[0].split('+'))
        for i in nums:
            result += int(i)
    else:        
        result = int(exp[0])

    judge = 1
    
    for i in range(judge, len(exp)):
        progress_minus = 0
        nums = list(exp[i].split('+'))
        for j in nums:
            progress_minus += int(j)
        result -= progress_minus

    print(result)