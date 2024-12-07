import tkinter as tk
from PIL import Image, ImageTk
import random

# Konfigurasi
layar_lebar = 800
layar_tinggi = 600
pipi_lebar = 80
pipi_tinggi = 300
burung_ukuran = 50
celah_pipa = 200
gravitasi = 0.5
kecepatan_lompat = -10
kecepatan_pipa = 5

class FlappyBirdGame:
    def __init__(self, root):
        self.root = root
        self.root.geometry(f"{layar_lebar}x{layar_tinggi}")
        self.canvas = tk.Canvas(self.root, width=layar_lebar, height=layar_tinggi)
        self.canvas.pack()

        # Load dan ubah ukuran gambar
        self.load_and_resize_images()

        self.init_game()

        self.root.bind("<space>", self.lompat)
        self.update()

    def load_and_resize_images(self):
        # Load dan ubah ukuran gambar burung
        self.original_bird_image = Image.open("test_folder/burung.png")
        self.resized_bird_image = self.original_bird_image.resize((burung_ukuran, burung_ukuran), Image.LANCZOS)
        self.burung_image = ImageTk.PhotoImage(self.resized_bird_image)
        
        # Load dan ubah ukuran gambar latar belakang
        self.original_bg_image = Image.open("test_folder/background.png")
        self.resized_bg_image = self.original_bg_image.resize((layar_lebar, layar_tinggi), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.resized_bg_image)

    def init_game(self):
        # Menghapus elemen canvas sebelumnya jika ada
        self.canvas.delete("all")

        # Tambahkan gambar latar belakang
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)

        self.burung_x = layar_lebar // 4
        self.burung_y = layar_tinggi // 2
        self.burung_vy = 0

        self.pipi_x = layar_lebar
        self.pipi_y_atas = random.randint(50, layar_tinggi - pipi_tinggi - celah_pipa)
        self.pipi_y_bawah = self.pipi_y_atas + pipi_tinggi + celah_pipa

        self.skor = 0

        self.burung = self.canvas.create_image(self.burung_x, self.burung_y, anchor="nw", image=self.burung_image)
        self.pipi_atas = self.canvas.create_rectangle(self.pipi_x, 0, self.pipi_x + pipi_lebar, self.pipi_y_atas, fill="grey")
        self.pipi_bawah = self.canvas.create_rectangle(self.pipi_x, self.pipi_y_bawah, self.pipi_x + pipi_lebar, layar_tinggi, fill="grey")
        self.teks_skor = self.canvas.create_text(layar_lebar // 2, 50, text="Skor: 0", font=("Arial", 24), fill="black")

    def lompat(self, event):
        self.burung_vy = kecepatan_lompat

    def update(self):
        self.burung_y += self.burung_vy
        self.burung_vy += gravitasi
        self.canvas.coords(self.burung, self.burung_x, self.burung_y)

        self.pipi_x -= kecepatan_pipa
        self.canvas.coords(self.pipi_atas, self.pipi_x, 0, self.pipi_x + pipi_lebar, self.pipi_y_atas)
        self.canvas.coords(self.pipi_bawah, self.pipi_x, self.pipi_y_bawah, self.pipi_x + pipi_lebar, layar_tinggi)

        if self.pipi_x < -pipi_lebar:
            self.pipi_x = layar_lebar
            self.pipi_y_atas = random.randint(50, layar_tinggi - pipi_tinggi - celah_pipa)
            self.pipi_y_bawah = self.pipi_y_atas + pipi_tinggi + celah_pipa
            self.skor += 1
            self.canvas.itemconfig(self.teks_skor, text=f"Skor: {self.skor}")

        if (self.burung_y < 0 or self.burung_y > layar_tinggi - burung_ukuran or
            (self.burung_x + burung_ukuran > self.pipi_x and self.burung_x < self.pipi_x + pipi_lebar and
             (self.burung_y < self.pipi_y_atas or self.burung_y + burung_ukuran > self.pipi_y_bawah))):
            self.canvas.itemconfig(self.teks_skor, text=f"Game Over! Skor: {self.skor}")
            self.root.unbind("<space>")
            self.tampilkan_tombol_ulangi()
        else:
            self.root.after(30, self.update)  # Menyesuaikan interval pembaruan untuk kecepatan yang lebih wajar

    def tampilkan_tombol_ulangi(self):
        self.tombol_ulangi = tk.Button(self.root, text="Ulangi", command=self.restart_game, font=("Arial", 14), bg="red", fg="white")
        self.tombol_ulangi.place(relx=0.5, rely=0.5, anchor="center")

    def restart_game(self):
        self.tombol_ulangi.destroy()
        self.init_game()
        self.root.bind("<space>", self.lompat)
        self.update()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    game = FlappyBirdGame(root)
    root.mainloop()
