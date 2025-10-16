n = int(input())

people_left = []

for i in range(n):
  name, el = input().split()
  
  if el == "enter":
    people_left.append(name)
  else:
    people_left.remove(name)
    
people_left.sort()
people_left.reverse()

for i in people_left:
  print(i)
  
  
  #dict로 해보자 시간초과ㅏㅏㅏ