total = int(input("input total purchasing: "))
if total <= 1000:
    print(total)
if total >= 1000:
    a = int(input("menggunakan kartu kredit(1.iya 2.tidak):"))
    if a == 1:
        print(total,"bonus payung")
    if a ==2 :
        print(total,"bonus gelas")