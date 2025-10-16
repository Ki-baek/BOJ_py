import sys
input = sys.stdin.readline

result = 0

while(1):
  n = int(input().strip())
  
  if n == -1:
    break
  
  result += n

print(result)