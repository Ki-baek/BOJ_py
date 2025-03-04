import sys
input = sys.stdin.readline


words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

string = input().strip()
length = len(string)
for i in words:
    if i in string:
        string.count(i)