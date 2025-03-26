import sys
input = sys.stdin.readline

n = int(input().strip())

end = 0
result = 0

info = [list(map(int, input().strip().split())) for i in range(n)]

info.sort(key = lambda x : (x[1], x[0]))

for nextstart, nextend in info:
    if end <= nextstart:
        result += 1
        end = nextend

print(result)

# 회의가 일찍 끝난다 == 더 많은 회의를 할수 있는 기회가 늘어난다
# sort에서 lambda 쓰는 법은 좀더 익숙해지기