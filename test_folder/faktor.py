num = int(input("Masukkan sebuah angka: "))
print(f"Faktor-faktor dari {num} adalah:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)