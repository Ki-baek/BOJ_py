n, m = map(int, input().split())

six = []
one = []

for i in range(m):
    a, b = map(int, input().split())

    six.append(a)
    one.append(b)

cheapest_six = sorted(six, reverse = True)
cheapest_one = sorted(one, reverse = True)

the_one = cheapest_one.pop()
the_six = cheapest_six.pop()

if_six = min(((n // 6) * the_six) + ((n % 6) * the_one), ((n // 6) + 1) * the_six)
if_one = n * the_one

print(min(if_six, if_one))