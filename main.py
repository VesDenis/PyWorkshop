class WordError(Exception):
  def __init__(self):
    self.message = 'This is your Exception message!'
    super().__init__(self.message)

def check_w_letter(word, letter):
  if letter in word:
    raise WordError
  else:
    print(word)

letter = input()
word = input()
check_w_letter(word, letter)