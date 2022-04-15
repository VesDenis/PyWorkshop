class NegativeSumException(Exception):
  def __init__(self, x):
    self.message = "Sum cannot be negative"
    super().__init__(self.message)

def sum_with_exceptions(a, b):
  if a + b < 0:
    raise NegativeSumException(a + b)
  else:
    print(a + b)

sum_with_exceptions(2, -5)