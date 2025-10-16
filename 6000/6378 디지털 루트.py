import sys
input = sys.stdin.readline


while(1):
  string = input().rstrip()
  if string == '0':
    break
  
  while(1):
    a = []
    for i in str(string):
      a.append(int(i))
  
    result = sum(a)
  
    if result < 10:
      print(result)
      break
    
    else:
      string = result