import sys
input = sys.stdin.readline

n = int(input().strip())

lst_people = []

for i in range(n):
    name = input().strip()
    if len(list(name)) == 3:
        lst_people.append(name)

length = len(lst_people)
candidate = lst_people[0]

for i in range(1, length):
    if candidate > lst_people[i]:
        candidate = lst_people[i]

print(candidate)