from random import shuffle, randint

def give(full):
    stock = full[:]
    pgive = []
    cgive = []
    start = 0
    while [5, 5] not in stock[:14] and [6, 6] not in stock[:14]:
        shuffle(stock)
    for double in [[6, 6], [5, 5]]:
        if double in stock[:14]:
            snake = [stock.pop(stock.index(double))]
    pgive = stock[:6]
    cgive = stock[6:13]
    if randint(0, 1):
        pgive, cgive = cgive, pgive
    if len(cgive) < len(pgive):
        start = 1
    stock = stock[13:]
    return stock, pgive, cgive, snake, start

def game():
    while True:
        print('Stock pieces:', len(stock))
        print('Computer pieces:', len(cgive))
        print(snake)
        print('Your pieces:')
        for i, piece in enumerate(pgive, start=1):
            print(i, piece)
        if snake[0][0] == snake[-1][1] and sum(snake, []).count(snake[0][0]) == 8 and len(snake) != 1:
            print("""Status: The game is over. It's a draw!""")
            break
        elif len(pgive) == 0:
            print('Status: The game is over. You won')
            break
        elif len(cgive) == 0:
            print('Status: The game is over. The computer won')
            break
        else:
            turn()

def player_d():
    try:
        num = int(input())
    except ValueError:
        print('Invalid input. Please try again.')
        player_d()
    else:
        snake.append(pgive.pop(num - 1))

def computer_d():
    enter = input()
    if enter != '':
        print('Invalid input. Please try again.')
        computer_d()
    else:
        snake.append(cgive.pop(randint(0, len(cgive) - 1)))

def turn():
    global start
    if start:
        print("""Status: It's your turn to make a move. Enter your command""")
        start -= 1
        player_d()
    else:
        print('Status: Computer is about to make a move. Press Enter to continue')
        start += 1
        computer_d()

full = [[i, j] for i in range(7) for j in range(i, 7)]
stock, pgive, cgive, snake, start = give(full)
game()