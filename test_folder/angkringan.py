import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import Frame, Label
from PIL import Image, ImageTk

master = tk.Tk()
master.title("Angkringan Murah")
master.config(bg="brown")

# Function to save data
def save_data():
    kode_kategori = kode_customer_entry.get()
    nama = nama_entry.get()
    jenis = alamat.get()
    harga = harga_entry.get()
    if kode_kategori and nama and jenis and harga:
        table.insert('', 'end', values=(kode_kategori, nama, jenis, harga))
        kode_customer_entry.delete(0, tk.END)
        nama_entry.delete(0, tk.END)
        alamat.set("")
        harga_entry.delete(0, tk.END)
        update_total()
    else:
        messagebox.showwarning("Input Error", "Semua kolom harus diisi!")

# Function to select data
def select_data(event):
    selected_item = table.selection()
    if selected_item:
        item_values = table.item(selected_item)['values']
        if item_values:
            kode_customer_entry.delete(0, tk.END)
            kode_customer_entry.insert(0, item_values[0])
            nama_entry.delete(0, tk.END)
            nama_entry.insert(0, item_values[1])
            alamat.set(item_values[2])
            harga_entry.delete(0, tk.END)
            harga_entry.insert(0, item_values[3])

# Function to update data
def update_data():
    selected_item = table.selection()
    if selected_item:
        table.item(selected_item, values=(kode_customer_entry.get(), nama_entry.get(), alamat.get(), harga_entry.get()))
        kode_customer_entry.delete(0, tk.END)
        nama_entry.delete(0, tk.END)
        alamat.set("")
        harga_entry.delete(0, tk.END)
        update_total()
    else:
        messagebox.showwarning("Update Error", "Pilih item untuk diperbarui!")

# Function to delete data
def delete_data():
    selected_item = table.selection()
    if selected_item:
        table.delete(selected_item)
        kode_customer_entry.delete(0, tk.END)
        nama_entry.delete(0, tk.END)
        alamat.set("")
        harga_entry.delete(0, tk.END)
        update_total()
    else:
        messagebox.showwarning("Delete Error", "Pilih item untuk dihapus!")

# Function to update total price
def update_total():
    total = 0
    for item in table.get_children():
        item_values = table.item(item)['values']
        total += float(item_values[3])
    total_label.config(text=f"Total Harga: {total}")

# Creating frame
frame = Frame(master, width=300, height=300, bg="white")
frame.grid(row=0, column=0, columnspan=3, pady=20)

# Adding image
image_path = r'test_folder/angkringan.png'
image = Image.open(image_path)
image = image.resize((400, 150), Image.Resampling.LANCZOS)
photo_image = ImageTk.PhotoImage(image)
image_label = Label(frame, image=photo_image)
image_label.pack()

# Creating labels and entries
kode_customer_label = tk.Label(master, text="Nomor Antrian")
nama_label = tk.Label(master, text="Nama Customer")
alamat_label = tk.Label(master, text="Menu")
harga_label = tk.Label(master, text="Harga")

kode_customer_label.grid(row=1, column=0, pady=10)
nama_label.grid(row=2, column=0, pady=10)
alamat_label.grid(row=3, column=0, pady=10)
harga_label.grid(row=4, column=0, pady=10)

kode_customer_entry = tk.Entry(master)
nama_entry = tk.Entry(master)
alamat = ttk.Combobox(master, values=["Ayam Geprek", "Ayam Penyet", "Nasi Kucing ", "Mie Goreng/Rebus", "Sate Kulit", "Ceker"])
harga_entry = tk.Entry(master)

kode_customer_entry.grid(row=1, column=1)
nama_entry.grid(row=2, column=1, pady=5)
alamat.grid(row=3, column=1, pady=5)
harga_entry.grid(row=4, column=1, pady=5)

# Creating table
columns = ('Nomor Antrian', 'Nama', 'Jenis', 'Harga')
table = ttk.Treeview(master, columns=columns, show='headings')
table.grid(row=6, column=0, columnspan=3, padx=(50, 50), pady=5, sticky=tk.W)

# Configuring table
table.heading('Nomor Antrian', text='Nomor Antrian')
table.heading('Nama', text='Nama Customer')
table.heading('Jenis', text='Menu')
table.heading('Harga', text='Harga')
table.column('Nomor Antrian', width=100)
table.column('Nama', width=100)
table.column('Jenis', width=250)

# Creating total price label
total_label = tk.Label(master, text="Total Harga: 0", bg="brown", fg="white")
total_label.grid(row=7, column=0, columnspan=3, pady=10)

# Button actions
save = tk.Button(master, text="Save", width=10, command=save_data)
update = tk.Button(master, text="Update", width=10, command=update_data)
delete = tk.Button(master, text="Delete", width=10, command=delete_data)
bersih = tk.Button(master, text="Bersih", width=10, command=lambda: [kode_customer_entry.delete(0, tk.END), nama_entry.delete(0, tk.END), alamat.set("")])

save.grid(row=5, column=0, padx=5, pady=20, sticky='w')
update.grid(row=5, column=1, padx=5, pady=20, sticky='w')
delete.grid(row=5, column=1, padx=5, pady=20, sticky='e')
bersih.grid(row=5, column=2, padx=5, pady=20, sticky='e')

# Bind row selection to fill fields
table.bind("<ButtonRelease-1>", select_data)

master.mainloop()
