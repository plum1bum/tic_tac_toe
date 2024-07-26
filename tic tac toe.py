board = [' ' for _ in range(9)]
current_player = 'X'


def print_board():
    print('-------------')
    for i in range(3):
        print(f'| {board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]} |')
        print('-------------')


def check_winner():
    for i in range(3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != ' ':
            return True
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return True
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        return True
    return False


def check_draw():
    return ' ' not in board


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def check():
    while True:
        move = (input(f'Игрок {current_player}, введите координаты (0-8): '))
        if not (move.isdigit()):
            print(" Введите число! ")
            continue

        move = int(move)

        if 0 > move or move > 8:
            print(" Координаты вне диапазона! ")
            continue

        return move


def replay():
    while True:

        otv = (input(f'Хотите сыграть ещё раз? (1 - ДА, 2 - НЕТ) '))
        if not (otv.isdigit()):
            print(" Введите число! ")
            continue

        otv = int(otv)

        if 0 > otv or otv > 2:
            print(" Введите 1 (ДА) или 2 (НЕТ)")
            continue

        return otv


def play_game():
    print_board()

    while True:

        move = check()

        if board[move] == ' ':
            board[move] = current_player

            print_board()

            if check_winner():
                print(' █░█░█ █ █▄░█ \n ▀▄▀▄▀ █ █░▀█')
                print(f'Игрок {current_player} победил!')
                break

            if check_draw():
                print('Ничья')
                break

            switch_player()

        else:
            print('Это место уже занято. Пожалуйста, выберите другое.')


while True:
    print(' █░█ █▀▀ █░░ █░░ █▀█ \n █▀█ ██▄ █▄▄ █▄▄ █▄█ ')
    print('~~~игра в крестики-нолики~~~')
    print(' ')
    play_game()
    otv = replay()
    if otv == 1:
        print('\n' * 100)
        board = [' ' for _ in range(9)]
        continue
    else:
        print(' █▀▀ █▀█ █▀█ █▀▄   █▀▄ ▄▀█ █▄█ \n █▄█ █▄█ █▄█ █▄▀   █▄▀ █▀█ ░█░')
        break


