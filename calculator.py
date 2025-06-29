import tkinter as tk
window = tk. Tk()
window.title("Ahmad's Calculator")
window.geometry("300x400")

window.configure(bg="#2c3e50")

entry = tk.Entry(window, font=("arial", 24), width=25, bd=5,
                 justify="right", bg="white", fg="#2c3e50")
entry.pack(pady=20)


def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(button_text))


def clear():
    entry.delete(0, tk. END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk. END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'c', '=', '+']
]

for row in buttons:
    frame = tk. Frame(window, bg="#2c3e50")
    frame.pack()
    for button in row:
        def action(x=button):
            if x == '=':
                calculate()
            elif x == 'c':
                clear()
            else:
                click(x)
        if button == '=':
            bg_color = "#2ecc71"
        elif button == 'c':
            bg_color = "#e74c3c"
        else:
            bg_color = "#3498db"
        tk. Button(frame, text=button, width=5, height=2, font=("arial", 19), bg=bg_color,
                   fg="white", command=lambda x=button: action(x)).pack(side=tk.LEFT, padx=5, pady=5)

window.mainloop()
