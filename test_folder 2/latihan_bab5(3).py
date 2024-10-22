# a) 2, 3, 4, 6, 8, 12, 16
a = 2
while a <= 16:
    print(a, end=", " if a < 16 else "\n")
    if a < 4:
        a += 1
    elif a < 8:
        a += 2
    elif a < 16:
        a += 4
    else:
        break
# b) 18,15,12,9,6,3
b = 18
while b >= 3:
    print(b, end=", " if b > 3 else "\n")
    b -= 3
# c) 0 ,7 ,14 ,21 ,28 ,35 ,42 ,49
for c in range(0, 8):
    print(c * 7, end=", " if c < 7 else "")