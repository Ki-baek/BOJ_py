import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pokemon = {input().strip() :(i + 1) for i in range(n)}
reverse_pokemon = {j: k for k, j in pokemon.items()}

for i in range(m):
    k = input().strip()
    if k.isnumeric():
        print(reverse_pokemon[int(k)])
    else:
        print(pokemon[k])
