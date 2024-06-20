import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(entry.get())
            # Round the result to 13 decimal places
            result = round(result, 13)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "←":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text[:-1])
    else:
        entry.insert(tk.END, text)

def on_key_press(event):
    key = event.char
    if key in "0123456789+-*/.":
        entry.insert(tk.END, key)
    elif key == "\r":
        on_enter_pressed()
    elif key == "\b":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text[:-1])

def on_enter_pressed():
    try:
        result = eval(entry.get())
        # Round the result to 10 decimal places
        result = round(result, 10)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

root.resizable(False,False)

entry = tk.Entry(root, font=('Helvetica', 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, sticky='nsew')

button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', '0', '=', '+',
    'C', '←'
]

row, col = 0, 0

for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font=('Helvetica', 15), padx=20, pady=20)
    button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
    button.bind("<Button-1>", on_button_click)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Configure grid weights to make it expandable
for i in range(2):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.bind("<Key>", on_key_press)  # Bind the keypress event

root.mainloop()
