d1=0
d2=1
n=int(input("masukan nilai deret : "))

for i in range(n):
    print(d1, end=' ')
    dc = d2 + d1
    d1 = d2
    d2 = dc  