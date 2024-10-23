datakaryawan = ['budi', 'bunga', 'alex', 'mawar', 'dani', 'sultan']
nama = input("Masukkan nama: ").lower()
if nama in datakaryawan:
    print(f"{nama} adalah karyawan.")
else:
    print(f"{nama} bukan karyawan.")