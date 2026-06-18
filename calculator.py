import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showwarning("Warning", "Please select an operation.")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x250")


title_label = tk.Label(root, text="Simple Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)


tk.Label(root, text="Enter First Number:").pack()
entry_num1 = tk.Entry(root, width=20)
entry_num1.pack()

tk.Label(root, text="Enter Second Number:").pack()
entry_num2 = tk.Entry(root, width=20)
entry_num2.pack()


tk.Label(root, text="Select Operation:").pack()

operation_var = tk.StringVar()
operation_var.set("+")

operations = ["+", "-", "*", "/"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.pack(pady=5)


calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10)


result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack()


root.mainloop()