from collections import defaultdict, Counter

s = 0
count = defaultdict(int)
with open('passwords.txt', 'r') as file:
  for line in file.readlines():
    for letter in line.strip():
      count[letter] += 1
      s += 1
count = Counter(count)
for per in count.most_common(5):
  print(per[0], '-', str(per[1] // (s // 100)) + '%')
last = [k for k, _ in count.items()][-5:]
for per in last:
  print(per, '-', str(count[per] / (s // 100)) + '%')