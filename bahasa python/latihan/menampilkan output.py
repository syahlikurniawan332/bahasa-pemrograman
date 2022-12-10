nama = input("nama : ")
umur = input("umur kamu : ")
alamat = input("alamat kamu : ")
status = input ("menikah/belum : ")
# menginput dari keyboard dan disimpan di variabel dengan format variabel = input
# (") untuk menampilkan keterangan ketika di input
print ("")
print ("hallo ", nama)
print ("umur saya ", umur)
print ("alamat saya ", alamat)
print ("saya",status,"menikah")
print ("")
#menampilkan hasil inputan keyboard
print ("%s, halo" %nama, "data kamu telah di verifikasi")
#menggunakan fungsi format () untuk menggabungkan isi variabel dengan teks dengan cara lama
print ("terimakasih {}, atas kunjungannya".format(nama))
#menggunakan fungsi format () untuk menggabungkan isi variabel dengan teks dengan cara sekarang