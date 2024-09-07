class TicTacToe:
    def __init__(self):
        self.data = [[" " for _ in range(3)] for _ in range(3)]

    def placeX(self, xindex, yindex):
        if self.is_valid_move(xindex, yindex):
            self.data[xindex][yindex] = "X"
            self.show_board()
            if self.check_winner("X"):
                print("X wins!")
                return True
            elif self.check_tie():
                print("tie")
                return True
            return False
        else:
            print("Invalid move. Try again.")
            return False

    def placeO(self, xindex, yindex):
        if self.is_valid_move(xindex, yindex):
            self.data[xindex][yindex] = "O"
            self.show_board()
            if self.check_winner("O"):
                print("O wins!")
                return True
            elif self.check_tie():
                print("tie!")
                return True
            return False
        else:
            print("Invalid move. Try again.")
            return False

    def is_valid_move(self, xindex, yindex):
        return 0 <= xindex < 3 and 0 <= yindex < 3 and self.data[xindex][yindex] == " "

    def check_winner(self, player):
        for row in self.data:
            if all([cell == player for cell in row]):
                return True
        for col in range(3):
            if all([self.data[row][col] == player for row in range(3)]):
                return True
        if all([self.data[i][i] == player for i in range(3)]) or \
           all([self.data[i][2-i] == player for i in range(3)]):
            return True
        return False

    def check_tie(self):
        return all([self.data[i][j] != " " for i in range(3) for j in range(3)])

    def game(self):
        self.show_board()
        for turn in range(9):
            if turn % 2 == 0:
                print("X's turn")
                xindex1 = int(input("Put X x index: "))
                yindex1 = int(input("Put X y index: "))
                if self.placeX(xindex1, yindex1):
                    break
            else:
                print("O's turn")
                xindex1 = int(input("Put O x index: "))
                yindex1 = int(input("Put O y index: "))
                if self.placeO(xindex1, yindex1):
                    break

    def show_board(self):
        for row in self.data:
            print("|".join([str(cell).center(3, " ") for cell in row]))
            print("-" * 9)

t1 = TicTacToe()
t1.game()
