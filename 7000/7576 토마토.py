import sys
input = sys.stdin.readline

M, N = map(int, input().strip().split())
judge = 1

def ripe(x, y):
    plus_x = [1, -1, 0, 0]
    plus_y = [0, 0, 1, -1]
    global judge

    for i in range(4):
        check_x = x + plus_x[i]
        check_y = y + plus_y[i]
        
        if (0 <= check_x < M) and (0 <= check_y < N) and tomato_box[check_y][check_x] == 0:
            tomato_box[check_y][check_x] = cnt + 1
            judge = 0

tomato_box = []

for i in range(N):
    tomato_box.append(list(map(int, input().strip().split())))


cnt = 1

while True:    

    for a in range(M):
        for b in range(N):
            if tomato_box[b][a] == cnt:
                ripe(a, b)
            

    cnt += 1

    if judge:
        break

    judge = 1


if 0 in (s_num for row in tomato_box for s_num in row):
    print(-1)

else:
    print(cnt - 2)


# cnt = 1로 놓고 cnt 주위에 0들을 cnt + 1로 바꾸어나가고 
# 한 사이클이 끝날 때 마다 cnt += 1하고
# 더이상 바꿀 0이 존재하지 않으면 끝내고
# 0이 남았는지 검사 ... mustaaaaaaaaaaaaaard 하고 없으면 cnt - 2 출력
# 있으면 -1 출력 근데 시간제한 2초인데 가능할깜?
# turn this tv off~ 일단 갈기자