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
entrada = tk.Entry(root, width=25, font=("Arial", 18), bg=entry_bg_color, fg=entry_text_color)
entrada.grid(row=0, column=0, columnspan=4, pady=10)

label_hasil = tk.Label(root, text="Hasil:", font=("Arial", 18), bg="#2c3e50", fg=result_text_color)
label_hasil.grid(row=1, column=0, columnspan=4, pady=10)

# Tombol Angka dan Operasi
buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '.', '='
]

row = 2
col = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=5, height=2, font=("Arial", 18),
                  command=eval_expression, bg=button_color, fg=button_text_color).grid(row=row, column=col, pady=5, padx=5)
    elif button == 'C':
        tk.Button(root, text=button, width=5, height=2, font=("Arial", 18),
                  command=clear, bg=button_color, fg=button_text_color).grid(row=row, column=col, pady=5, padx=5)
    else:
        tk.Button(root, text=button, width=5, height=2, font=("Arial", 18),
                  command=lambda button=button: click(button), bg=button_color, fg=button_text_color).grid(row=row, column=col, pady=5, padx=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
