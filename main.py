try:
  print("What a beautiful name you have!")
except NameError:
  print("Hello, stranger!")
else:
  print("Hello,", name)
finally:  
  print("Hope to see you soon!")