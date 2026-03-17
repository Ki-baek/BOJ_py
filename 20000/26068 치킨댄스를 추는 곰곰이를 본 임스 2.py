n = int(input())

cnt = 0

for i in range(n):
  dayLeft = list(input())
  dayLeft.remove('D')
  dayLeft.remove('-')
  day = int(''.join(dayLeft))
  
  if day <= 90:
    cnt += 1
  else:
    continue
  
print(cnt)