#penjumlahan
def f_jumlah (a,b):
    hasil = a + b
    print("hasil penjumlahana : ",hasil)
    print("")
    return hasil

#pengurangan
def f_kurang (a , b):
    hasil = a - b
    print("hasil pengurangan: ",hasil)
    print("")
    return hasil

#perkalian
def f_kali (a , b):
    hasil = a * b
    print("hasil kali: ",hasil)
    print("")
    return hasil

#bagi
def f_bagi (a , b):
    hasil = a / b
    print("hasil bagi: ",+ hasil)
    print("")
    return hasil

#sisa pembagian
def f_sisa_bagi (a , b):
    hasil = a % b
    print("hasil sisa bagi: ",hasil)
    print("")
    return hasil

#perpangkatan
def f_pangkat (a , b):
    hasil = a ** b
    print("hasil pangkat: ",hasil)
    print("")
    return hasil

#opsional
def menu():
    print("pili opsi aritmatika yang diinginkan")
    print("====================================================")
    print("[1] penjumlahan")
    print("[2] pengurangan")
    print("[3] perkalian")
    print("[4] pembagian")
    print("[5] sisa pembagian")
    print("[6] pemangkatan")
    print("====================================================")
menu()

hasil = int(input("pilihan menu : "))

if hasil == 1:
    a = int(input("Masukkan nilai: "))
    b = int(input("Masukkan nilai: "))
    hasil= f_jumlah(a,b)
    print ("Hasil:", hasil)
elif hasil == 2:
    a = int(input("Masukkan nilai: "))
    b = int(input("Masukkan nilai: "))
    f_kurang(a,b)
elif hasil == 3:
    a = int(input("Masukkan nilai: "))
    b = int(input("Masukkan nilai: "))
    f_kali(a,b)
elif hasil == 4:
    a = int(input("Masukkan nilai: "))
    b = int(input("Masukkan nilai: "))
    f_bagi(a,b)
elif hasil == 5:
    a = int(input("Masukkan nilai: "))
    b = int(input("Masukkan nilai: "))
    f_sisa_bagi(a,b)
elif hasil == 6:
    a = int(input("Masukkan nilai: "))
    b = int(input("Masukkan nilai: "))
    f_pangkat(a,b)
else:
    print("tidak ada dalam menu")
