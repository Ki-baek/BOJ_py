import sys

string = sys.stdin.readline().rstrip()

str = list(string.lower())
lst = [0] * 123
while str:
  k = str.pop()
  lst[ord(k)] += 1
max_value = max(lst)

judge = 0

for i in lst:
  if i == max_value:
    judge += 1

if judge > 1:
  print('?')
  sys.exit()

max_key = lst.index(max_value)

print((chr(max_key)).upper())


#lower / upper method의 존재 유무가 상당히 와닫는 문제.. 함수는 많이 알수록 좋다
