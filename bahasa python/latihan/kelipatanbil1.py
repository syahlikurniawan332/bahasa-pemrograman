bil1=int(input("masukan nilai bil1 : "))
bil2=int(input("masukan nilai bil2 : "))
n=15

kelipatan=bil1
for i in range (n):
    if(kelipatan<n):
        print("hasil kelipatan ",kelipatan)
    
    kelipatan += bil2