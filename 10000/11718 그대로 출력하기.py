import sys

string = list()

for i in sys.stdin:
  string.append(i.rstrip())

print('\n'.join(string))