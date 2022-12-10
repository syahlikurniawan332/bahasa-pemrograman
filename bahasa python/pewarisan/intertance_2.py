class ComputerPart:
    def __init__(self, pabrikan, nama, jenis, harga):
        self.pabrikan=pabrikan
        self.nama=nama
        self.jenis=jenis
        self.harga=harga
        
class processor (ComputerPart) :
    def __init__(self, pabrikan, nama, harga, jumlah_core, speed):
        super().__init__(pabrikan, nama, 'processor', harga)
        self.jumlah_core=jumlah_core
        self.speed=speed

class RandomAccessMemory(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas):
        super().__init__(pabrikan, nama, 'RAM' ,harga)
        self.kapasitas=kapasitas
        
class HardDiskSATA(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm):
        super().__init__(pabrikan, nama, 'SATA', harga)
        self.kapasitas=kapasitas
        self.rpm=rpm
        
p=processor('Intel','Core I7',4350000,4,'4.3GHz')
m=RandomAccessMemory('V-gen','DDR',236000,'4GB')
hdd=HardDiskSATA('seagate','HDD',2950000,'500000',7200)

parts = [p,m,hdd]

for part in parts:
    print('{} {} produk{}'.format(part.jenis,part.nama,part.pabrikan))