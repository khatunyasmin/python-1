import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display and input numbers
entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Function to update the Entry widget
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Define numeric buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and position numeric buttons
row_val = 1
col_val = 0

for button_text in buttons:
    if button_text == '=':
        btn = tk.Button(root, text=button_text, padx=20, pady=20, command=lambda: eval_expression())
    else:
        btn = tk.Button(root, text=button_text, padx=20, pady=20, command=lambda button_text=button_text: button_click(button_text))
    btn.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Function to evaluate the expression
def eval_expression():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Run the main loop
root.mainloop()
