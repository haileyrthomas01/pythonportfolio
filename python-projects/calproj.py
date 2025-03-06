import tkinter as tk

def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    result_label.config(text="Result: " + str(result))

def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    result_label.config(text="Result: " + str(result))

def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    result_label.config(text="Result: " + str(result))

def divide():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    if num2 != 0:
        result = num1 / num2
        result_label.config(text="Result: " + str(result))
    else:
        result_label.config(text="Error: Cannot divide by zero")

#create the main window
window = tk.Tk()
window.title("Calculator")
window.configure(bg="#273ea5")

#create title label
title_label = tk.Label(window, text="Calculator", font=("Arial", 24, "bold"), bg="#273ea5")
title_label.pack(pady=10)

#create input fields
entry1 = tk.Entry(window)
entry1.pack(pady=5)

entry2 = tk.Entry(window)
entry2.pack(pady=5)

#create buttons
add_button = tk.Button(window, text="Add", command=add, bg="#586cc3", fg="black")
add_button.pack(pady=5)

subtract_button = tk.Button(window, text="Subtract", command=subtract, bg="#8493d6", fg="black")
subtract_button.pack(pady=5)

multiply_button = tk.Button(window, text="Multiply", command=multiply, bg="#b6c0ee", fg="black")
multiply_button.pack(pady=5)

divide_button = tk.Button(window, text="Divide", command=divide, bg="#d6ddff", fg="black")
divide_button.pack(pady=5)

#create result label
result_label = tk.Label(window, text="Result: ")
result_label.pack(pady=5)

# Run the main window loop
window.mainloop()
