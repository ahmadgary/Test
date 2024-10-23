import tkinter as tk
from tkinter import messagebox

def check_grade():
    try:
        nilai = int(entry.get())
        if nilai >= 86:
            grade = "A  Sangat Baik"
        elif nilai >= 76:
            grade = "B Baik"
        elif nilai >= 66:
            grade = "C Cukup"
        elif nilai >= 56:
            grade = "D  Kurang"
        else:
            grade = "E Gagal"
        messagebox.showinfo("Hasil", grade)
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai yang valid")

# Create the main window
root = tk.Tk()
root.title("Penilaian Siswa")

# Create and place the widgets
label = tk.Label(root, text="Masukkan Nilai Siswa:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Cek Predikat", command=check_grade)
button.pack(pady=20)

# Run the application
root.mainloop()
