email = input()
i = 0
while email[i] != '@':
  i += 1
print(email[:i])