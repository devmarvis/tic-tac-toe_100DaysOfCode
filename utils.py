

class Game:
    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.replay = ''

    def print_board(self):
        for i in range(0, 9, 3):
            print(f' {self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}')
            if i < 6:
                print('---|---|---')

    def check_winner(self, user, symbl):
        if self.board[user] != ' ':
            self.print_board()
            print('Space already filled, Try again!')
            self.replay = symbl

        else:
            self.board[user] = symbl
            self.print_board()
            self.replay = ''

        for i in range(0, len(self.board), 3):
            mid_col = 1
            r_dia = 2
            if self.board[i] != ' ' and self.board[i] == self.board[i+1] == self.board[i+2]:
                self.print_board()
                print(f'Winner is Player {self.board[i]}')
                return True

            if i + 1 == mid_col:
                if self.board[mid_col] != ' ' and self.board[mid_col] == self.board[mid_col+3] == self.board[mid_col+6]:
                    self.print_board()
                    print(f'Winner is Player {self.board[i + 1]}')
                    return True

            if i % 3 == 0 and i < 3:
                if self.board[i] != ' ' and self.board[i] == self.board[i + 4] == self.board[i + 8]:
                    self.print_board()
                    print(f'Winner is Player {self.board[i]}')
                    return True
                elif self.board[i] != ' ' and self.board[i] == self.board[i + 3] == self.board[i + 6]:
                    self.print_board()
                    print(f'Winner is Player {self.board[i]}')
                    return True

            if i % 3 == 0 and i - 1 == r_dia:
                if self.board[r_dia] != ' ' and self.board[r_dia] == self.board[r_dia + 2] == self.board[r_dia + 4]:
                    self.print_board()
                    print(f'Winner is Player {self.board[i - 1]}')
                    return True
                elif self.board[r_dia] != ' ' and self.board[r_dia] == self.board[r_dia + 3] == self.board[r_dia + 6]:
                    self.print_board()
                    print(f'Winner is Player {self.board[i - 1]}')
                    return True

