s = 0
with open('passwords.txt', 'r') as file:
  for word in file:
      s += 1
print(s)