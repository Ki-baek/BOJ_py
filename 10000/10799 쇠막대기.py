from collections import deque
import sys
input = sys.stdin.readline

lst = list(input().rstrip())
stack = []
result = 0

for i in range(len(lst)):
  if lst[i] == '(':
    stack.append(1)
  elif lst[i] == ')' and lst[i - 1] == '(':
    result += len(stack)
  else:
    stack.pop()

print(result)