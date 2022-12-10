# class person
class person() :
    #fungsi_init_sebagai_konstruktur
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    
    def display(self):
        print(self.name)
        print(self.idnumber)
        
#child class (kelas anak)
class Employee(person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        
        #looking the _init_of the parent class
        person.__init__(self, name, idnumber)
    
    def detail(self):
        print("my name is {}".format(self.name))
        print("idnumber : {}".format(self.idnumber))
        print("post : {}".format(self.post))
        
#membuat objek variabel
a = Employee('sahli',2021573010019,500000,"lecture")

#memanggil fungsi dari class person
a.display()
a.detail()