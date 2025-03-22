import sys
input = sys.stdin.readline

grade = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0': 3.0, 'C+' : 2.5, 'C0': 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F': 0.0}
result = 0
cnt = 0

for i in range(20):

    lst = list(input().strip().split())
    lst[1] = float(lst[1])

    if lst[2] != 'P':
        result += lst[1] * grade[lst[2]]
        cnt += lst[1]

print(result / cnt)