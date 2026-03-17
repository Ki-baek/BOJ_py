t = int(input())

for i in range(t):
  sides = sorted(list(map(int, input().split())))
  
  a = sides[0]
  b = sides[1]
  c = sides[2]
  
  if a + b <= c:
    print(f"Case #{i + 1}: invalid!") 
  
  elif a == b == c:
    print(f"Case #{i + 1}: equilateral")
  elif a == b or b == c or c == a:
    print(f"Case #{i + 1}: isosceles")
  else:
    print(f"Case #{i + 1}: scalene")