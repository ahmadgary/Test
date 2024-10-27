angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

lebih_besar = max(angka1, angka2)

while True:
    if lebih_besar % angka1 == 0 and lebih_besar % angka2 == 0:
        kpk = lebih_besar
        break
    lebih_besar += 1

print(f"KPK dari {angka1} dan {angka2} adalah {kpk}")
