T = int(input())

for i in range(T):
  a, b = map(int, input().split())
  
  lst = []
  k = a % 10
  
  if k == 0:
    print(10)
    continue
  
  while k not in lst:
    
    lst.append(k)
    k = (k * a) % 10
  
  n =  (b - 1) % len(lst)
  
  print(lst[n])