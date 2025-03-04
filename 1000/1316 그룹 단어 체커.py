import sys
input = sys.stdin.readline
from collections import deque

n = int(input().strip())

appeared = set()
count = 0

for i in range(n):
    judge = True
    letter = '0'
    word = deque(input().strip())
    while word:
        if letter != word[0]:
            letter = word.popleft()

            if letter not in appeared:
                appeared.add(letter)
            else:
                judge = False
                break
        else:
            word.popleft()
    
    if judge:
        count += 1
    
    appeared.clear()
print(count)