a = list(map(int, input().split()))
ans = 0
for i in range(len(a) - 1):
  j = i + 1
  while a[j] - a[i] <= 3 and j < len(a) - 1:
    j += 1
  if j != len(a) - 1:
    ans += len(a[j:])
print(ans)