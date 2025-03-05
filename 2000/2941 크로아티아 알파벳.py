import sys
input = sys.stdin.readline

words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


string = input().strip()

for i in words:
    if i in string:
        string = string.replace(i, 'a')

print(len(string))