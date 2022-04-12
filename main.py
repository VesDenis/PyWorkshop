from random import randint

def shift(a):
  k = randint(1, len(a) - 1) * -1
  a = a[k:] + a[:k]
  return a

def search(a):
  arr = a[:]
  l = a[len(a) - 1]
  if a[0] < a[len(a) - 1]:
    return a[len(a) - 1]
  else:
    while arr[len(arr) // 2] < a[len(arr) // 2 + 1]:
      if arr[len(arr) // 2] < l:
        arr = arr[:len(arr) // 2]
      else:
        arr = arr[len(arr) // 2:]
      print(arr)
    return arr[len(arr) // 2]
      

a = [_ for _ in range(1, 11)]
a.sort()
a = shift(a)
print(a)
print(search(a))