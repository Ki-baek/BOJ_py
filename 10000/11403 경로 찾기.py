import sys
input = sys.stdin.readline

n = int(input().rstrip())

arr = []

for i in range(n):
  arr.append(list(map(int, input().rstrip().split())))

for k in range(n):
  for i in range(n):
    for j in range(n):
      if arr[i][k] and arr[k][j]:
        arr[i][j] = 1
        
for i in arr:
  for j in i:
    print(j, end = ' ')
  print()
  
  # 플로이드-워셜 알고리즘을 이용하거나 DFS를 이용하기
  # 이 알고리즘의 핵심은 중간 노드를 이용해야함
  # A, B, C 세 노드를 잡고 B를 중간 노드라고 하면 B의 값을 증가시키며 A, C간의 최단거리를 구하는게 이 알고리즘의 핵심임
  