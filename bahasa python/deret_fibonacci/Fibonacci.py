#Fungsi Deret Fibonacci secara Looping dan Non-Rekursif
def fib(n):
    bil1 = 1
    bil2 = 1
    print ("|", bil1, end = " | ")
    while bil1 <= n:
        print(bil2, end=" | ")
        bil_lain = bil1 + bil2
        bil1 = bil2
        bil2 = bil_lain
        if bil2 > n :
            break
    print(' ')
print ("===Fungsi untuk menampilkan Deret Fibonacci Secara Looping dan Non-Rekursif===")
fib(1000)
print("================================================================================")
#Fungsi Deret Fibonacci secara Rekursif
def fibonacci(bil1,bil2, n):
    if bil1 <= n or bil2 <= n:
        print ("|", bil1, end = " | ")
        bil_lain = bil1 + bil2
        bil1 = bil2
        bil2 = bil_lain
        fibonacci(bil1,bil2, n)

print ("===Fungsi untuk menampilkan Deret Fibonacci Secara Rekursif===")
bil1 = int(input ("Masukkan nilai bil1 = "))
bil2 = int(input ("Masukkan nilai bil2 = "))
n = int (input("Masukkan nilai n : "))

fibonacci(bil1,bil2,n)