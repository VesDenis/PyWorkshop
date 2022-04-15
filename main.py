class NotInBoundsError(Exception):
  def __str__(self):
    return 'There is an error!'

def error_handling(func):
  def wrapper(*args):
    try:
      n = func(*args)
    except NotInBoundsError as err:
      print(err)
    else:
      return n
  return wrapper

@error_handling
def check_integer(num):
  if 45 < num < 67:
    raise NotInBoundsError
  else:
    print(num)

check_integer(44)