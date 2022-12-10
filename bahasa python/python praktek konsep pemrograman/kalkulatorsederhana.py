print(20*"=")
print("kalkulator sederhana")
print(20*"=")

#kalkulator dimulai
angka_1 = float(input("masukkan angka 1="))
operator = input("(+,-,/,x) :")
angka_2 = float(input("masukkan angka yang ke 2="))

#percabangan
if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah{hasil}")
elif operator == "x" or operator=="*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adlaah {hasil}")
else :
    print("error taek makanya jangan goblok")

