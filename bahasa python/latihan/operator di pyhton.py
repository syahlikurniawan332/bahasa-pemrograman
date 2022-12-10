#operator merupakan simbol yang digunakan untuk melakukan operasi tertentu
# ada 6 jenis operator yakni, aritmatika,pembandingan,penugasan,logika,bitwise,ternary

#operator aritmatika
a= int(input ("masukan nilai a : "))
b= int(input ("masukan nilai b : "))

#penjumlahan
c = a + b
print("a + b = ", c)

#pengurangan
c = a - b
print("a - b = ", c)

#perkalian
c = a * b
print("a * b = ", c)

#pembagian
c = a / b
print("a / b = ", c)

#sisa bagi
c = a % b
print("a % b = ", c)

#pangkat
c = a ** b
print("a ** b = ", c)

#operator penugasan
d = int(input("nilai d : "))
# tambahkan dengan 5
d += 5
# kurangi 3
d -= 3
# kali 10
d /= 4
# pangkat 10
d **= 10

#berapakah nilai d sekarang
print("nilai d adalah ", d)
