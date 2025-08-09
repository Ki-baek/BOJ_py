import sys
input = sys.stdin.readline

string = list(input().rstrip())
judge = True
length = len(string)

for i in range(length // 2):
  if string[i] != string[length - i - 1]:
    judge = False
    break
  
if judge == True:
  print(1)

else:
  print(0)  