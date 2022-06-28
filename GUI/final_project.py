import tkinter as tk
from tkinter.messagebox import showerror


def main():
    PocketCalculator().mainloop()


class PocketCalculator(tk.Tk):
    buttons = []

    def __init__(self):
        super().__init__()
        self.title("Pocket calculator")
        self.resizable(False, False)
        self.geometry("150x120")

        self.place_widgets()
        self.add_commands()

    def place_widgets(self):
        self.entry = tk.Entry(self)
        self.entry.insert(0, "0")
        self.entry.pack(fill=tk.BOTH)

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack(fill=tk.BOTH)

        # Place digits from 1 to 9
        row_number = 0
        column_number = 2
        for i in range(9, 0, -1):
            button = tk.Button(self.buttons_frame, text=str(i), width=3)
            button.grid(row=row_number // 3, column=column_number)
            self.buttons.append(button)
            row_number += 1
            column_number = 2 if column_number == 0 else column_number - 1

        for index, text in enumerate(["0", "C", ".", "="]):
            button = tk.Button(self.buttons_frame, text=text, width=3)
            button.grid(row=3, column=index)
            self.buttons.append(button)

        for index, text in enumerate(["+", "-", "*", "/"]):
            button = tk.Button(self.buttons_frame, text=text, width=3)
            button.grid(row=index, column=4)
            self.buttons.append(button)

    def reset_entry(self, event=None):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, "0")

    def evaluate_expression(self, event=None):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except SyntaxError:
            showerror("Error", "Syntax Error")
        except ZeroDivisionError:
            showerror("Error", "Zero Division Error")

    def update_entry(self, event=None):
        if self.entry.get() == "0":
            self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, event.widget["text"])

    def add_commands(self):
        for button in self.buttons:
            if button["text"] == "C":
                button.bind("<Button-1>", self.reset_entry)
            elif button["text"] == "=":
                button.bind("<Button-1>", self.evaluate_expression)
            else:
                button.bind("<Button-1>", self.update_entry)


if __name__ == "__main__":
    main()
