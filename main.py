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
    while len(arr) > 2 and arr[len(arr) // 2] <= arr[len(arr) // 2 + 1]:
      if arr[len(arr) // 2] < l:
        arr = arr[:len(arr) // 2]
      else:
        arr = arr[len(arr) // 2:]
      print(arr)
    if(len(arr) == 2):
      if (arr[0] > arr[1]):
        return arr[0]
      else:
        return arr[1]
    return arr[len(arr) // 2]
      

a = [randint(1, 20) for _ in range(randint(2, 20))]
a = sorted(a)
a = shift(a)
print(a)
print(search(a))