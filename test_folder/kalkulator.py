import tkinter as tk

def eval_expression():
    try:
        expression = entrada.get()
        hasil = eval(expression)
        label_hasil.config(text=f"Hasil: {hasil}", fg="white")
    except ZeroDivisionError:
        label_hasil.config(text="Tidak boleh dibagi 0!", fg="red")
    except Exception:
        label_hasil.config(text="Error!", fg="red")

def click(button):
    current_text = entrada.get()
    new_text = current_text + button
    entrada.delete(0, tk.END)
    entrada.insert(0, new_text)

def clear():
    entrada.delete(0, tk.END)
    label_hasil.config(text="Hasil:", fg="white")

def backspace():
    current_text = entrada.get()
    new_text = current_text[:-1]
    entrada.delete(0, tk.END)
    entrada.insert(0, new_text)

root = tk.Tk()
root.title("Kalkulator")

# Gaya dan warna
root.configure(bg="#2c3e50")
button_color = "#3498db"
button_text_color = "#ecf0f1"
entry_bg_color = "#34495e"
entry_text_color = "#ecf0f1"
result_text_color = "#ecf0f1"

# Tampilan Entri dan Hasil
entrada = tk.Entry(root, font=("Arial", 18), bg=entry_bg_color, fg=entry_text_color)
entrada.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")

label_hasil = tk.Label(root, text="Hasil:", font=("Arial", 18), bg="#2c3e50", fg=result_text_color)
label_hasil.grid(row=1, column=0, columnspan=4, pady=10, sticky="nsew")

# Tombol Angka dan Operasi
buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '.', '=', '(', ')'
]

row = 2
col = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=5, height=2, font=("Arial", 18),
                  command=eval_expression, bg=button_color, fg=button_text_color).grid(row=row, column=col, pady=5, padx=5, sticky="nsew")
    elif button == 'C':
        tk.Button(root, text=button, width=5, height=2, font=("Arial", 18),
                  command=clear, bg=button_color, fg=button_text_color).grid(row=row, column=col, pady=5, padx=5, sticky="nsew")
    else:
        tk.Button(root, text=button, width=5, height=2, font=("Arial", 18),
                  command=lambda button=button: click(button), bg=button_color, fg=button_text_color).grid(row=row, column=col, pady=5, padx=5, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Tombol Backspace
tk.Button(root, text='⌫', width=5, height=2, font=("Arial", 18), command=backspace, bg=button_color, fg=button_text_color).grid(row=row, column=col, pady=5, padx=5, sticky="nsew")

# Konfigurasi pengaturan grid untuk mendukung resizing
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(row+1):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
