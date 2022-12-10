from class_kalkulator import kalkulator_sederhana as kal

print("Menu: ")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Faktorial")
print("4. Pemangkatan")
menu = int(input("Pilih operasi: "))

a = int(input("Masukkan Nilai-1 = "))
b = int(input("Masukkan Nilai-2 = "))

if(menu == 1):
    hasil = kal.penjumlahan(a,b)
    print("Hasil Penjumlahan = ", hasil)
elif(menu == 2):
    hasil = kal.pengurangan(a,b)
    print("Hasil Pengurangan = ", hasil)
elif(menu == 3):
    hasil = kal.faktorial(a,b)
    print("Hasil Faktroial = ", hasil)
elif(menu == 4):
    hasil = kal.pemangkatan(a,b)
    print("Hasil Pemangkatan = ", hasil)
