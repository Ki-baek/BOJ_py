a, b = map(str, input().split())

da = list(a)
db = list(b)

da.reverse()
db.reverse()

a = int(''.join(da))
b = int(''.join(db))

if a > b:
  print(a)
else:
  print(b)