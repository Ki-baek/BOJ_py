import sys
input = sys.stdin.readline

t = int(input())
dic = {1 : 1, 2 : 2, 3 : 4}

for i in range(7):
    dic[i + 4] = dic[i + 3] + dic[i + 2] + dic[i + 1]
    
for i in range(t):
    n = int(input())
    print (dic[n])