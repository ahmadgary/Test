total_belanja = float(input("Masukkan total belanja Budi: "))

print(f"Total belanja: Rp{total_belanja}")

if total_belanja > 300:
    diskon = 0.15 * total_belanja
    total_setelah_diskon = total_belanja - diskon
    print("Diskon: 15%")
else:
    diskon = 0
    total_setelah_diskon = total_belanja
    print("Diskon: 0%")

print(f"Total yang harus dibayar: Rp{total_setelah_diskon:.2f}")