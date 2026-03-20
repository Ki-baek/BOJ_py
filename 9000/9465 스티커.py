import sys
input = sys.stdin.readline

t = int(input().rstrip())


for i in range(t):
  
  sticker = []
  n = int(input().rstrip())
  
  sticker.append(list(map(int, input().rstrip().split())))
  sticker.append(list(map(int, input().rstrip().split())))
  
  max_score = max(sticker)
  index = sticker.index(max_score)
  
  
  