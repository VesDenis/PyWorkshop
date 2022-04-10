def rec(a, b):
  if a == b:
    return 1
  else:
    return rec(a + 1, b)

a, b = map(int, input().split())
print(rec(a, b))