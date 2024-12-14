import tkinter as tk
from PIL import Image, ImageTk
import random
import pygame  # Tambahkan impor pygame

# Konfigurasi
layar_lebar = 800  # Perbesar lebar layar
layar_tinggi = 800  # Perbesar tinggi layar
pipi_lebar = 100  # Perbesar lebar pipa
pipi_tinggi = 200  # Tinggi pipa default
jarak_pipa_vertikal = 100  # Jarak vertikal antara pipa atas dan pipa bawah
jarak_pipa_horizontal = 400  # Jarak horizontal antara pipa yang berturut-turut
burung_ukuran = 50  # Perbesar ukuran burung
gravitasi = 0.2
kecepatan_lompat = -4

class FlappyBird:
    def __init__(self):
        # Inisialisasi Pygame Mixer untuk musik
        pygame.mixer.init()
        pygame.mixer.music.load("test_folder/music.mp3")
        pygame.mixer.music.play(-1)  # Mainkan musik berulang kali

        self.root = tk.Tk()
        self.root.geometry(f"{layar_lebar}x{layar_tinggi}")
        self.canvas = tk.Canvas(self.root, width=layar_lebar, height=layar_tinggi)
        self.canvas.pack()

        self.load_and_resize_images()  # Panggil fungsi untuk memuat dan mengubah ukuran gambar

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

        self.burung_x = layar_lebar // 2
        self.burung_y = layar_tinggi // 2
        self.burung_vy = 0

        self.pipi_x1 = layar_lebar
        self.pipi_x2 = layar_lebar + jarak_pipa_horizontal

        self.pipi_y_atas1, self.pipi_y_bawah1 = self.generate_pipe_heights()
        self.pipi_y_atas2, self.pipi_y_bawah2 = self.generate_pipe_heights()

        self.skor = 0

        self.burung = self.canvas.create_image(self.burung_x, self.burung_y, anchor="nw", image=self.burung_image)
        self.pipi1_atas = self.canvas.create_rectangle(self.pipi_x1, 0, self.pipi_x1 + pipi_lebar, self.pipi_y_atas1, fill="grey")
        self.pipi1_bawah = self.canvas.create_rectangle(self.pipi_x1, self.pipi_y_bawah1, self.pipi_x1 + pipi_lebar, layar_tinggi, fill="grey")
        self.pipi2_atas = self.canvas.create_rectangle(self.pipi_x2, 0, self.pipi_x2 + pipi_lebar, self.pipi_y_atas2, fill="grey")
        self.pipi2_bawah = self.canvas.create_rectangle(self.pipi_x2, self.pipi_y_bawah2, self.pipi_x2 + pipi_lebar, layar_tinggi, fill="grey")
        self.teks_skor = self.canvas.create_text(layar_lebar // 2, 50, text="Skor: 0", font=("Arial", 24))

    def lompat(self, event):
        self.burung_vy = kecepatan_lompat

    def update(self):
        self.burung_y += self.burung_vy
        self.burung_vy += gravitasi
        self.canvas.coords(self.burung, self.burung_x, self.burung_y)

        self.pipi_x1 -= 3  # Pindahkan pipa pertama ke kiri
        self.pipi_x2 -= 3  # Pindahkan pipa kedua ke kiri
        self.canvas.coords(self.pipi1_atas, self.pipi_x1, 0, self.pipi_x1 + pipi_lebar, self.pipi_y_atas1)
        self.canvas.coords(self.pipi1_bawah, self.pipi_x1, self.pipi_y_bawah1, self.pipi_x1 + pipi_lebar, layar_tinggi)
        self.canvas.coords(self.pipi2_atas, self.pipi_x2, 0, self.pipi_x2 + pipi_lebar, self.pipi_y_atas2)
        self.canvas.coords(self.pipi2_bawah, self.pipi_x2, self.pipi_y_bawah2, self.pipi_x2 + pipi_lebar, layar_tinggi)

        if self.pipi_x1 < -pipi_lebar:
            self.pipi_x1 = layar_lebar
            self.pipi_y_atas1, self.pipi_y_bawah1 = self.generate_pipe_heights()
            self.skor += 1
            self.canvas.itemconfig(self.teks_skor, text=f"Skor: {self.skor}")

        if self.pipi_x2 < -pipi_lebar:
            self.pipi_x2 = layar_lebar
            self.pipi_y_atas2, self.pipi_y_bawah2 = self.generate_pipe_heights()
            self.skor += 1
            self.canvas.itemconfig(self.teks_skor, text=f"Skor: {self.skor}")

        if (self.burung_y < 0 or self.burung_y > layar_tinggi - burung_ukuran or
            (self.burung_x + burung_ukuran > self.pipi_x1 and self.burung_x < self.pipi_x1 + pipi_lebar and
             (self.burung_y < self.pipi_y_atas1 or self.burung_y + burung_ukuran > self.pipi_y_bawah1)) or
            (self.burung_x + burung_ukuran > self.pipi_x2 and self.burung_x < self.pipi_x2 + pipi_lebar and
             (self.burung_y < self.pipi_y_atas2 or self.burung_y + burung_ukuran > self.pipi_y_bawah2))):
            self.canvas.itemconfig(self.teks_skor, text=f"Game Over! Skor: {self.skor}")
            self.root.unbind("<space>")
            self.tampilkan_tombol_ulangi()
        else:
            self.root.after(16, self.update)

    def generate_pipe_heights(self):
        # Mengatur posisi pipa dengan jarak vertikal tetap
        pipa_y_atas = random.randint(50, layar_tinggi - pipi_tinggi - jarak_pipa_vertikal)
        pipa_y_bawah = pipa_y_atas + pipi_tinggi + jarak_pipa_vertikal
        return pipa_y_atas, pipa_y_bawah

    def tampilkan_tombol_ulangi(self):
        self.tombol_ulangi = tk.Button(self.root, text="Restart", command=self.restart_game, font=("Arial", 14), bg="red", fg="white")
        self.tombol_ulangi.place(relx=0.5, rely=0.5, anchor="center")

    def restart_game(self):
        self.tombol_ulangi.destroy()
        self.init_game()
        self.root.bind("<space>", self.lompat)
        self.update()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = FlappyBird()
    game.run()
