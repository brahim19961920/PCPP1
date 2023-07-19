from random import randint
import tkinter as tk


def move_button(event=None):
    global button_abs, button_ord
    old_abs, old_ord = button_abs, button_ord

    while abs(old_abs - button_abs) < 100 and abs(old_ord - button_ord) < 100:
        button_abs, button_ord = randint(0, 400), randint(0, 400)

    button.place(x=button_abs, y=button_ord)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Catch me!")
    window.minsize(500, 500)
    window.maxsize(500, 500)

    button_abs, button_ord = 0, 0
    button = tk.Button(text="Catch me!")
    button.place(x=button_abs, y=button_ord)
    button.bind("<Motion>", move_button)

    window.mainloop()
