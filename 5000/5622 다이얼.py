dial = ['ABC', 'DEF','GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

string = list(input())
result = 0

for j in range(len(string)):
  for i in dial:
    if string[j] in i:
      result += dial.index(i) + 3

print(result)