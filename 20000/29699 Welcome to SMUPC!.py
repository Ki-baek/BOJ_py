string =list('0WelcomeToSMUPC')

n = int(input())
index = n % 14
if index == 0:
  index = 14

print(string[index])