import tkinter as tk

def click(event):
    global operator
    operator += str(event)
    text_input.set(operator)

def clear():
    global operator
    operator = ""
    text_input.set("")

def evaluate():
    global operator
    try:
        total = str(eval(operator))
        text_input.set(total)
        operator = total
    except:
        text_input.set(" error ")
        operator = ""

# Initialize the main window
calculator = tk.Tk()
calculator.title("Simple Calculator")

# Text input variable
operator = ""
text_input = tk.StringVar()

# Display screen
display = tk.Entry(calculator, font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4, width=14, justify='right')
display.grid(columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', 'C',
    '4', '5', '6', '+',
    '1', '2', '3', '-',
    '0', '*', '/', '='
]

row = 1
col = 0
for button in buttons:
    if button == "C":
        tk.Button(calculator, text=button, padx=20, pady=20, bd=8, fg='black', font=('arial', 20, 'bold'), command=clear).grid(row=row, column=col)
    elif button == "=":
        tk.Button(calculator, text=button, padx=20, pady=20, bd=8, fg='black', font=('arial', 20, 'bold'), command=evaluate).grid(row=row, column=col)
    else:
        tk.Button(calculator, text=button, padx=20, pady=20, bd=8, fg='black', font=('arial', 20, 'bold'), command=lambda button=button: click(button)).grid(row=row, column=col)
    col += 1
    if col == 4:
        col = 0
        row += 1

calculator.mainloop()
