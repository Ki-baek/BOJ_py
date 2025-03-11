import sys
input = sys.stdin.readline

n = int(input().strip())

for i in range(n):
    count = 0

    n_score = list(map(int, input().split()))

    aver = (sum(n_score) - n_score[0]) // n_score[0]

    for j in range(1, len(n_score)):
        if n_score[j] > aver:
            count += 1
    
    percentage = count / n_score[0] * 100

    print("%0.3f%%" % percentage)