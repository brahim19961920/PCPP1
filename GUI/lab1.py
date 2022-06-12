"""
Create a simple caculator. Lab 1 of GUI course.
"""

import tkinter as tk
from tkinter import messagebox


def evaluate():
    error_message = ""

    field1_value = field1.get()
    field2_value = field2.get()
    operator = str(string_var.get())

    if not field1_value:
        error_message = "Field 1 empty!"

    elif not field2_value:
        error_message = "Field 2 empty!"

    elif operator == "None":
        error_message = "No opertaor selected!"

    if error_message:
        messagebox.showerror("Error", error_message)
        return

    try:
        operation = f"{field1_value} {operator} {field2_value}"
        messagebox.showinfo("Result", f"{operation} = {str(eval(operation))}")
    except ZeroDivisionError:
        messagebox.showerror("Error", "ZeroDivisionError")


if __name__ == "__main__":

    window = tk.Tk()
    window.title("Calculator")

    string_var = tk.StringVar()
    string_var.set(None)

    # Define widgets
    field1 = tk.Entry()
    field2 = tk.Entry()
    sum_op = tk.Radiobutton(text="+", variable=string_var, value="+")
    sub_op = tk.Radiobutton(text="-", variable=string_var, value="-")
    mul_op = tk.Radiobutton(text="*", variable=string_var, value="*")
    div_op = tk.Radiobutton(text="/", variable=string_var, value="/")
    evaluate_button = tk.Button(text="Evaluate", command=evaluate)

    # place widgets on the main window
    field1.grid(column=0, row=2)
    sum_op.grid(column=1, row=0)
    sub_op.grid(column=1, row=1)
    mul_op.grid(column=1, row=3)
    div_op.grid(column=1, row=4)
    field2.grid(column=2, row=2)
    evaluate_button.grid(column=1, row=5)

    window.mainloop()
