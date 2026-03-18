result = 0

while True:
  
  try:
    n = int(input())
    result += n
  
  except EOFError:
    break

print(result)