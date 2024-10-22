i = (int(input("Masukkan angka: ")))
if i % 3 == 0 and i % 5 == 0:
    print("Papa Mama")
elif i % 3 == 0:
    print("Papa")
elif i % 5 == 0:
    print("Mama")
else:
    print(i)