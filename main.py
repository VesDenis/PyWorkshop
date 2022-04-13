from random import randint

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
revenues = [randint(1000, 3001) for _ in range(12)]
profits = [0] + [revenues[i] - revenues[i - 1] for i in range(1, 12)]
percents = [int(profits[i] / revenues[i] * 100) for i in range(12)]
words = []
for percent in percents:
  if percent > 50:
    words.append('great')
  elif percent > 25 and percent <= 50:
    words.append('decent')
  elif percent >= 0 and percent <= 25:
    words.append('need follow up')
  else:
    words.append('critical')
percents = [str(percents[i]) + '%' for i in range(12)]
percents[0] = 'n/a'
words[0] = 'n/a'
for month, profit, percent, word in zip(months, profits, percents, words):
  print(month, profit, percent, word)