class person:
    def __init__(self, nama, umur, size, hair_color):
        self.nama=nama
        self.umur=umur
        self.size=size
        self.hair_color=hair_color

class student(person):
    def __init__(self, nama, umur, size, hair_color, kelas):
        super().__init__(nama, umur, 'student', size, hair_color)
        self.kelas=kelas
        
class teacher(person):
    def __init__(self, nama, umur, size, hair_color, mengajar):
        super().__init__(nama, umur, 'teacher' , size, hair_color)
        self.mengajar=mengajar
        
s=student('wahyu','19',167,'hitam')
t=teacher('robi','22',177,'botak')
parts = [s,t]

for part in parts:
    print('{} {} age {} {}'.format(part.nama,part.size,part.hair_color))