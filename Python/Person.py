
# Saya Silmi Aulia Rohmah mengerjakan Latihan 4 DPBO 2022 C1 
# dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan 
# kecurangan seperti yang telah dispesifikasikan. Aamiin 


from time import sleep


class Person:

    def __init__(self): #Constructor

        self.Nik = ""
        self.Name = ""
        self.Gender = ""

    # metode getter dan setter
    def getNik(self):
        return self.Nik
    
    def setNik(self, Nik):
        self.Nik = Nik

    def getName(self):
        return self.Name
    
    def setName(self, Name):
        self.Name = Name

    def getGender(self):
        return self.Gender
    
    def setGender(self, Gender):
        self.Gender = Gender

    def sleep(self):

        print(self.getName() + " is sleeping..")

    # prosedur untuk print informasi class
    def getPersons(self):

        self.sleep()
        print("NIK            : " + self.getNik())
        print("Name           : " + self.getName())
        print("Gender         : " + self.getGender())

