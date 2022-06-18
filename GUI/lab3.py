from random import randint
import tkinter as tk
from tkinter.messagebox import showinfo


class Clicker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Clicker")
        self.buttons_list = []
        self.buttons_numbers = []
        button_number = randint(0, 1000)
        self.timer_value = 0

        for i in range(25):

            while str(button_number) in self.buttons_numbers:
                button_number = randint(0, 1000)

            self.buttons_numbers.append(str(button_number))
            new_button = tk.Button(self, text=str(button_number), width=10, height=2)
            new_button.bind("<Button -1 >", self.test)
            new_button.grid(row=len(self.buttons_list) // 5, column=len(self.buttons_list) % 5)
            self.buttons_list.append(new_button)

        self.timer_label = tk.Label(self, text="0", height=2)
        self.timer_label.grid(row=6, column=2)
        self.buttons_numbers.sort(key=lambda x: int(x))
        self.id = self.timer_label.after(1000, self.increase_time_value)

        self.mainloop()

    def test(self, event=None):

        if len(self.buttons_numbers) > 1:

            if event.widget["text"] == str(self.buttons_numbers[0]):
                del self.buttons_numbers[0]
                event.widget["bg"] = "red"
                event.widget["state"] = "disable"

        else:
            event.widget["bg"] = "red"
            event.widget["state"] = "disable"
            self.timer_label.after_cancel(self.id)
            showinfo("Game finished", f"You took {self.timer_label['text']} seconds to finish the game.")

    def increase_time_value(self):
        self.timer_value += 1
        self.timer_label.configure(text=str(self.timer_value))
        self.timer_label.after_cancel(self.id)
        self.id = self.timer_label.after(1000, self.increase_time_value)


if __name__ == "__main__":
    clicker = Clicker()
    clicker.mainloop()
