from random import randint
import tkinter as tk
from tkinter import messagebox


class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("TicTacToe")

        self.buttons = []
        self.user_buttons = []
        self.computer_buttons = []
        self.valid_combinaisons = [
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

        self.add_buttons()

    def add_letter(self, button, text, color):
        button.configure(text=text, fg=color)

    def click(self, event=None):
        if self.user_buttons in self.valid_combinaisons:
            messagebox.showinfo("Info", "You won the game")
            return

        elif self.computer_buttons in self.valid_combinaisons:
            messagebox.showinfo("Info", "You lost the game")
            return

        if event.widget["text"] == "":
            self.add_letter(event.widget, "O", "green")
            self.user_buttons.append(self.buttons.index(event.widget))
        else:
            return

        if self.user_buttons.sort() in self.valid_combinaisons:
            messagebox.showinfo("Info", "You lost the game")
            return

        button = self.buttons[randint(0, 8)]

        while button["text"] != "":
            button = self.buttons[randint(0, 8)]

        self.add_letter(button, "X", "red")
        self.computer_buttons.append(self.buttons.index(button))

        if self.computer_buttons.sort() in self.valid_combinaisons:
            messagebox.showinfo("Info", "You lost the game")
            return

    def add_buttons(self):
        for i in range(9):
            button = tk.Button(
                self,
                text="" if i != 4 else "X",
                fg="red",
                font=("Sans", 9, "bold"),
                width=10,
                height=5,
                padx=2,
                pady=2,
                justify="center",
            )
            button.grid(row=i // 3, column=i % 3)
            button.bind("<Button - 1>", self.click)
            self.buttons.append(button)
            # self.buttons[button] = {"clicked": False if i != 4 else True}


t = TicTacToe()
t.mainloop()
print(t.user_buttons, t.computer_buttons)
