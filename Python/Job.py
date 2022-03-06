
# Saya Silmi Aulia Rohmah mengerjakan Latihan 4 DPBO 2022 C1 
# dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan 
# kecurangan seperti yang telah dispesifikasikan. Aamiin 


class Job:

    def __init__(self): #Constructor

        self.Nip = ""
        self.companyName = ""
        self.position = ""

    # metode getter dan setter
    def getNIP(self):
        return self.Nip
    
    def setNIP(self, Nip):
        self.Nip = Nip

    def getCompanyName(self):
        return self.companyName
    
    def setCompanyName(self, companyName):
        self.companyName = companyName

    def getPosition(self):
        return self.position
    
    def setPosition(self, position):
        self.position = position

    # prosedur untuk print informasi class
    def getJob(self):
        print("NIP            : " + self.getNIP())
        print("Company Name   : " + self.getCompanyName())
        print("Position       : " + self.getPosition())