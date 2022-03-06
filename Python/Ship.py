
# Saya Silmi Aulia Rohmah mengerjakan Latihan 4 DPBO 2022 C1 
# dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan 
# kecurangan seperti yang telah dispesifikasikan. Aamiin 


from Vehicle import Vehicle

class Ship(Vehicle):

    
    def __init__(self): #Constructor

        self.countryOfManufacture = ""
        self.speed = 0
        self.grossTonnage = 0

    # metode getter dan setter
    def getCountryOfManufacture(self):
        return self.countryOfManufacture
    
    def setCountryOfManufacture(self, countryOfManufacture):
        self.countryOfManufacture = countryOfManufacture

    def getSpeed(self):
        return self.speed
    
    def setSpeed(self, speed):
        self.speed = speed

    def getGrossTonnage(self):
        return self.grossTonnage
    
    def setGrossTonnage(self, grossTonnage):
        self.grossTonnage = grossTonnage


    # prosedur untuk print informasi class
    def getShip(self):
        
        print("Country Of Manufacture  : " + self.getCountryOfManufacture())
        print("Speed                   : " + str(self.getSpeed()) + " mph")
        print("Gross Tonnage           : " + str(self.getGrossTonnage()) + " GT")
        print()