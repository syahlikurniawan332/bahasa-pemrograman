def pengurangan(a,b):
    hasil = a-b
    return hasil

def penjumlahan(a,b):
    hasil = a+b
    return hasil

def faktorial(a,b):
    faktorial = b

    for i in range(1, a + 1):
        faktorial *= i
        print(i)

    print(f'{a}! ')
    return faktorial

def pemangkatan(a,b):
    basis = a
    pangkat = b
    hasil = 1

    i = 0

    while i < pangkat:
        hasil = hasil * basis
        i += 1
    return hasil

print("Menu: ")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Faktorial")
print("4. Pemangkatan")
menu = int(input("Pilih operasi: "))

a = int(input("Masukkan Nilai-1 = "))
b = int(input("Masukkan Nilai-2 = "))

if(menu == 1):
    hasil = penjumlahan(a,b)
    print("Hasil Penjumlahan = ", hasil)
elif(menu == 2):
    hasil = pengurangan(a,b)
    print("Hasil Pengurangan = ", hasil)
elif(menu == 3):
    hasil = faktorial(a,b)
    print("Hasil Faktroial = ", hasil)
elif(menu == 4):
    hasil = pemangkatan(a,b)
    print("Hasil Pemangkatan = ", hasil)


