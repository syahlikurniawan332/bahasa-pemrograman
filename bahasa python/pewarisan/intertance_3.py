class Jam:
    def __init__(self, pabrikan, nama, jenis, harga):
        self.pabrikan=pabrikan
        self.nama=nama
        self.jenis=jenis
        self.harga=harga
        
class processor (Jam) :
    def __init__(self, pabrikan, nama, harga, jumlah_core, speed):
        super().__init__(pabrikan, nama, 'Bostante', harga)
        self.jumlah_core=jumlah_core
        self.speed=speed

class RandomAccessMemory(Jam):
    def __init__(self, pabrikan, nama, harga, kapasitas):
        super().__init__(pabrikan, nama, 'RAM' ,harga)
        self.kapasitas=kapasitas
        
class HardDiskSATA(Jam):
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm):
        super().__init__(pabrikan, nama, 'rating', harga)
        self.kapasitas=kapasitas
        self.rpm=rpm
        
p=processor('Bostante','smartwatch',4350000,4,'4.3GHz')
m=RandomAccessMemory('V-gen',3,236000,'4GB')
hdd=HardDiskSATA('shope',10,2950000,'500000',7200)

parts = [p,m,hdd]

for part in parts:
    print('{} {} produk{}'.format(part.jenis,part.nama,part.pabrikan))