def dfs():
  if len(result) == m:
    print(' '.join(map(str,result)))
    
    return

  last_num = 0 # 이게 다른 N과 M 문제랑 다른점. 초기 last_num 값은 0으로 설정
  
  for i in range(1, n + 1):
    
    if visited[i] == 0 and sorted_list[i - 1] != last_num:# last_num과 이번에 들어갈 숫자가 같다면 skip
      
      visited[i] += 1
      result.append(sorted_list[i - 1])
      last_num = sorted_list[i - 1]# 처음에 짰던 코드는 and 연산자와 append의 반복된 사용으로 복잡했던 과정을 변수 하나 더 써서 간단히함
      dfs()
      
      visited[i] -= 1
      result.pop()

    


n, m = map(int,input().split())

sorted_list = sorted(list(map(int, input().split())))

result = []

pre = []

visited = [0] * (n + 1)

dfs()