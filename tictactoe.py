import tkinter as tk
from tkinter import messagebox

# Create a Tic Tac Toe game class
class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [['' for _ in range(3)] for _ in range(3)]

        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.configure(background='light blue')

        # Create buttons for the game grid
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text="", width=10, height=5,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                button.configure(background='light blue')
                row.append(button)
            self.buttons.append(row)

    def make_move(self, row, col):
        # Check if the selected cell is empty
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.buttons[row][col].configure(text=self.current_player)

            # Check for a winner or a tie
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.window.quit()
            elif self.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.window.quit()
            else:
                # Switch players
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        # Check rows
        for i in range(3):
            if self.board[i] == [player, player, player]:
                return True

        # Check columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] == player:
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False

    def check_tie(self):
        for row in self.board:
            if '' in row:
                return False
        return True

    def run(self):
        self.window.mainloop()

# Create an instance of the Tic Tac Toe game
game = TicTacToe()
game.run()
