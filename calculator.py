import tkinter as tk

def click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())  # Caution: eval() can be dangerous with untrusted input
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        print(f"Error during calculation: {e}") #Print for debugging

# Main window
window = tk.Tk()
window.title("Calculator")

# Entry widget for display
entry = tk.Entry(window, width=30, borderwidth=10)
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, padx=20, pady=20, command=lambda b=button: click(b) if b not in ['=', 'C'] else calculate() if b == '=' else clear() if b == 'C' else None).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(window, text="C", padx=20, pady=20, command=clear).grid(row=5, column=0) #clear button

window.mainloop()