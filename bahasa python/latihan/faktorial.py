from re import I


bil1=int(input("masukan nilai bil1 : "))

faktorial=1
for i in range (1, bil1+1):
    faktorial*=i
    
    print(f"{bil1} ! = {faktorial }",end=' ')