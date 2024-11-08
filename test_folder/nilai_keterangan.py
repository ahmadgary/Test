import tkinter as tk
from tkinter import ttk, messagebox

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
        # Gunakan message box dari ttk untuk tampilan yang lebih modern
        style = ttk.Style()
        style.theme_use('clam')
        messagebox.showinfo("Hasil", grade)
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai yang valid")

# Create the main window
root = tk.Tk()
root.title("Penilaian Siswa")
root.geometry("300x200")
root.configure(bg="#f5f5f5")

# Create and place the widgets
frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(pady=20)

label = tk.Label(frame, text="Masukkan Nilai Siswa:", font=("Helvetica", 12), bg="#f5f5f5")
label.pack(pady=5)

entry = tk.Entry(frame, font=("Helvetica", 12), width=15)
entry.pack(pady=5)

button = tk.Button(frame, text="Cek Predikat", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=check_grade)
button.pack(pady=10)

# Run the application
root.mainloop()
