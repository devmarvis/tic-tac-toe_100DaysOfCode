from utils import Game


game = Game()

n = 0
# winner = False

while n < 9:
    game.print_board()
    if not game.replay:
        print('Player X')
        user_X = int(input('Mark where?\n>> ')) - 1
        if game.check_winner(user_X, 'X'):
            break
        elif game.replay:
            continue

        print('Player O')
        user_O = int(input('Mark where?\n>> ')) - 1
        if game.check_winner(user_O, 'O'):
            break
        elif game.replay:
            continue
    else:
        print(f'Player {game.replay}')
        user = int(input('Mark where?\n>> ')) - 1
        if game.check_winner(user, game.replay):
            break
        elif game.replay:
            continue

    n += 1

if not n < 9:
    print('DRAW, GAME OVER!')

