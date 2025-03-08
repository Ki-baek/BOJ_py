def dfs():
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return
    
    for i in range(1, n + 1):

        if visited[i] == 0:# i가 나온적 없으면

            visited[i] += 1# i가 등장한 적 있다는 표시
            lst.append(i)# i를 제?작중인 순열에 포함
            dfs()# dfs함수 재귀 >> 순열의 길이가 m이 되는지 확인 후, 아니라면 for문 다시 반복 > 그런데 visited[0](== 1)이 0이 아니므로 2로 넘어가서 순차 진행 + 재귀
            lst.pop() #재귀가 끝났다면 순열에서 하나씩 제거 + 남은 for 문 반복하며 순열 가짓수 더 탐색
            visited[i] = 0


n, m = map(int, input().split())

lst = []

visited = [0] * (n + 1)

dfs()