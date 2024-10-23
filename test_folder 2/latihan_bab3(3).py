total_belanja = float(input("Masukkan Total Belanja: "))
bonus = "-"
diskon = 0
diskon_text = "0%"
total_bayar = total_belanja

if total_belanja > 500000:
    bonus = "Mug Cantik"
    diskon_text = "7%"
    diskon = 0.07 * total_belanja
    total_bayar = total_belanja - diskon
elif total_belanja >= 100000 and total_belanja <= 499000:
    bonus = "Coca Cola"
    diskon_text = "5%"
    diskon = 0.05 * total_belanja
    total_bayar = total_belanja - diskon

print(f'Bonus: {bonus}')
print(f'Diskon: {diskon_text}')
print(f'Total Diskon: {diskon:.1f}')
print(f'Total Bayar: {total_bayar}')
