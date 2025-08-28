t = int(input())

for i in range(t):
  
  a, b = map(int, input().split())
  j = a * b
  if a == b:
    print(a)
  
  elif a > b:
    
    k = a % b
    while k != 0:
      a = b
      b = k
      k = a % b
    print(j // b)
    
  else:
    
    k = b % a
    while k != 0:
      b = a
      a = k
      k = b % a
    print(j // a)