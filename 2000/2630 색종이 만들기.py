import sys
input = sys.stdin.readline

def div_paper(x, y, k):
    color = paper[y][x]
    for i in range(y, y + k):
        for j in range(x, x + k):
            if color != paper[i][j]:
                l = k // 2
                div_paper(x, y + l, l)
                div_paper(x + l, y, l)
                div_paper(x, y, l)
                div_paper(x + l, y + l, l)
                return
    
    if color == 0:
        result[0] += 1
    else:
        result[1] += 1



n = int(input().strip())
paper = []

for i in range(n):
    paper.append(list(map(int, input().split())))


result = [0] * 2

div_paper(0, 0, n)

print(result[0], '\n',result[1], sep = '')