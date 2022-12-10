total = int(input("total yang harus di bayar: "))
bayar = total

if total > 1000000:
    print("kamu mendapat diskon")

    diskon = total * 20/100
    bayar = total - diskon

print("total yang harus dibayar: ", bayar)
