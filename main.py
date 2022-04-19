s = 0
with open('summer.txt', 'r', encoding='utf-8') as file:
  for word in file:
    if word.strip() == 'summer':
      s += 1
print(s)