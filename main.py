N ,D = map(int, input().split())
d = list(map(int, input().split()))
for i in range(len(d) - 1):
  for j in range(i + 1, len(d)):
    if sum(d[i:j]) >= D:
      break
  if sum(d[i:j]) == D:
    print(i + 1, j + 1)
    break