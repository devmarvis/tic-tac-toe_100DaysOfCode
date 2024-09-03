
def print_board(board_):

    for i in range(0, 9, 3):
        print(f' {board_[i]} | {board_[i+1]} | {board_[i+2]}')
        if i < 6:
            print('---|---|---')


board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

print_board(board)

n = 0
winner = False

while n < 9:
    user_X = int(input('Mark where?\n>> ')) - 1
    if board[user_X] != ' ':
        print_board(board)
        print('Space already filled, Try again!')
        user_X = int(input('Mark where?'))
    else:
        board[user_X] = 'X'
        print_board(board)

    for i in range(0, len(board), 3):
        if board[i] != ' ' and board[i] == board[i+1] == board[i+2]:
            print(f'Winner is User {board[i]}')
            print_board(board)
            winner = True
            break

        if i % 3 == 0 and i < 3:
            if board[i] != ' ' and board[i] == board[i + 4] == board[i + 8]:
                print(f'Winner is User {board[i]}')
                print_board(board)
                winner = True
                break

    if winner:
        break





