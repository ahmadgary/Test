angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

while angka2:
    angka1, angka2 = angka2, angka1 % angka2

print(f"FPB dari kedua angka adalah {angka1}")
