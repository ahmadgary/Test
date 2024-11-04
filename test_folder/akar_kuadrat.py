# Memasukkan angka dari pengguna
angka = int(input("Masukkan angka: "))

# Menghitung akar kuadrat
akar_kuadrat = angka ** 0.5

# Menampilkan hasil tanpa .0 jika hasil adalah bilangan bulat
if akar_kuadrat.is_integer():
    print(f"Akar kuadrat dari {angka} adalah {int(akar_kuadrat)}")
else:
    print(f"Akar kuadrat dari {angka} adalah {akar_kuadrat}")