board = [[' ' for x in range(3)] for y in range(3)]

def print_board():
    for row in board:
        print("|".join(row))

def check_win(player):
    
    for row in board:
        if row == [player, player, player]:
            return True
    
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def play():
    while True:
        print_board()
        x, y = input("Игрок 1, введите координаты (x y): ").split()
        x, y = int(x), int(y)
        if board[x][y] != ' ':
            print("Недопустимый ход!")
            continue
        board[x][y] = 'X'
        if check_win('X'):
            print_board()
            print("Игрок 1 победил!")
            break
        print_board()
        x, y = input("Игрок 2, введите координаты (x y): ").split()
        x, y = int(x), int(y)
        if board[x][y] != ' ':
            print("Недопустимый ход!")
            continue
        board[x][y] = 'O'
        if check_win('O'):
            print_board()
            print("Игрок 2 победил!")
            break

play()
