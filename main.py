from random import choice
####

def dset():
    return [[i, j] for i in range(7) for j in range(i, 7)]

def give(full):
    stock = full[:]
    pgive = []
    cgive = []
    for i in range(7):
        now = choice(stock)
        pgive.append(now)
        stock.remove(now)
    for i in range(7):
        now = choice(stock)
        cgive.append(now)
        stock.remove(now)
    if([5, 5] in stock or [6, 6] in stock):
        give(full)
    return stock, pgive, cgive


full = dset()
stock, pgive, cgive = give(full)
if([6, 6] in cgive):
    snake = [6, 6]
    cgive.remove([6, 6])
elif ([6, 6] in pgive):
    snake = [6, 6]
    pgive.remove([6, 6])
elif ([6, 6] in stock and [5, 5] in cgive):
    snake = [5, 5]
    cgive.remove([5, 5])
elif ([6, 6] in stock and [5, 5] in pgive):
    snake = [5, 5]
    pgive.remove([5, 5])
print('Stock pieces ', stock)
print('Computer pieces ', cgive)
print('Player pieces ', pgive)
print('Domino snake ', snake)
if len(cgive) < len(pgive):
    print('Status: player')
else:
    print('Status: computer')