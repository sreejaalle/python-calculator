import math
import tkinter as tk
from tkinter import messagebox

# Function to evaluate mathematical expressions
def calculate():
    try:
        expression = entry.get()  # Get user input
        result = eval(expression)  # Evaluate the expression
        entry.delete(0, tk.END)  # Clear the input field
        entry.insert(0, str(result))  # Show the result
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed!")
        entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")
        entry.delete(0, tk.END)

# Function to insert text into the input field
def insert_text(text):
    entry.insert(tk.END, text)

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Function to delete the last character (Backspace)
def backspace():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text[:-1])  # Remove the last character

# Create the main GUI window
root = tk.Tk()
root.title("Advanced Calculator")

# Input field
entry = tk.Entry(root, width=40, borderwidth=5, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout (including Backspace)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('Clear', 5, 0), ('(', 5, 1), (')', 5, 2), ('√', 5, 3),
    ('Backspace', 6, 0), ('sin', 6, 1), ('cos', 6, 2), ('tan', 6, 3),
    ('log', 7, 0)
]

# Add buttons to the GUI
for text, row, col in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=10, height=2, command=calculate)
    elif text == 'Clear':
        button = tk.Button(root, text=text, width=10, height=2, command=clear)
    elif text == 'Backspace':
        button = tk.Button(root, text=text, width=10, height=2, command=backspace)
    elif text == '√':
        button = tk.Button(root, text=text, width=10, height=2, command=lambda: insert_text('math.sqrt('))
    elif text in ['(', ')']:
        button = tk.Button(root, text=text, width=10, height=2, command=lambda t=text: insert_text(t))
    elif text in ['sin', 'cos', 'tan', 'log']:
        button = tk.Button(root, text=text, width=10, height=2, command=lambda t=text: insert_text(f'math.{t}('))
    else:
        button = tk.Button(root, text=text, width=10, height=2, command=lambda t=text: insert_text(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the GUI event loop
root.mainloop()



