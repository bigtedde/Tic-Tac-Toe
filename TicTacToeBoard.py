# Tik-Tac-Toe game created by Ted Lawson on 1/1/23
# Created following a tutorial on https://realpython.com/tic-tac-toe-python/#demo-a-tic-tac-toe-game-in-python

import tkinter as tk
from tkinter import font

def main():
    return

class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe game")
        self._cells = {}


if __name__ == "__main__":
    main()
