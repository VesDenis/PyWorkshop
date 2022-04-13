a = int(input())
b = int(input())

try:
  result = a / b
except ZeroDivisionError:
  print('Error')  # err is exception description
else:
  print(result)