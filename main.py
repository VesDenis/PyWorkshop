from collections import defaultdict, Counter

s = 0
count = defaultdict(int)
with open('passwords.txt', 'r') as file:
  for line in file.readlines():
    for letter in line.strip():
      count[letter] += 1
      s += 1
  count = Counter(count)
  mi = s * count.most_common(1)[0][1]
  ans = ''
with open('passwords.txt', 'r') as file:
  for line in file.readlines():
    su = 0
    for l in line.strip():
      su += count[l]
    if su < mi:
      mi = su
      ans = line
print(ans)