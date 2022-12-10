
class kalkulator_sederhana:

    def pengurangan(a, b):
        hasil = a - b
        return hasil

    def penjumlahan(a, b):
        hasil = a + b
        return hasil

    def faktorial(a, b):
        faktorial = b

        for i in range(1, a + 1):
            faktorial *= i
            print(i)

        print(f'{a}! ')
        return faktorial

    def pemangkatan(a, b):
        basis = a
        pangkat = b
        hasil = 1

        i = 0

        while i < pangkat:
            hasil = hasil * basis
            i += 1
        return hasil
