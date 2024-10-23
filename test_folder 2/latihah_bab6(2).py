hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
input_hari = int(input("Masukkan angka (1-7): "))
if 1 <= input_hari <= 7:
    print(f"Hari: {hari[input_hari - 1]}")
else:
    print("Input tidak valid. Masukkan angka antara 1 hingga 7.")
