dial = list(input())

'''phone = {3 : ['A', 'B', 'C'], 4 : ['D', 'E', 'F'], 5 : ['G', 'H', 'I'], 6 : ['J', 'K', 'L'], 
         7 : ['M','N','O'], 8 : ['P', 'Q', 'R', 'S'], 9 : ['T', 'U', 'V'], 10 : ['W', 'X', 'Y', 'Z']}'''

phone_target = {v : k for k, v in phone.items()}

while dial:
  letter = dial.pop()
  phone_target.get(letter)