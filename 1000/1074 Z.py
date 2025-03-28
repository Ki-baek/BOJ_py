#분할정복 사분면을 계~속 쪼개가며 찾아야됨

n, r, c = map(int, input().split())
result = 0

while n != 0:

    n -= 1

    if r < (2 ** n):

        if c < (2 ** n):
            result += (2 ** n) * (2 ** n) * 0
        
        else:
            result += (2 ** n) * (2 ** n) * 1
            c -= (2 ** n)

    else:

        if c < (2 ** n):
            result += (2 ** n) * (2 ** n) * 2
            r -= (2 ** n)
        
        else:
            result += (2 ** n) * (2 ** n) * 3
            c -= (2 ** n)
            r -= (2 ** n)


print(result)

# line 8이 코드의 핵?심인 것 같음
# n - 1이 코드 단순화에 기여가 상당히 큼
# 규칙 찾는게 중요한 문제 같아보이면 무작정 박지말고 생각좀 하기