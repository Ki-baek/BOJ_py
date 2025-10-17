import sys
input = sys.stdin.readline

entry_log = dict()

n = int(input().rstrip())

for i in range(n):
  a, b = input().rstrip().split()
  
  if b == 'enter':
    entry_log[a] = b
    
  else:
    del entry_log[a]

entry_log = sorted(entry_log.keys(), reverse=True)

for i in entry_log:
  print(i)