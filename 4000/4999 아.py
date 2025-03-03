import sys
input = sys.stdin.readline

jh = list(input().strip())
dr = list(input().strip())

if jh.count('a') >= dr.count('a'):
    print('go')
else:
    print('no')