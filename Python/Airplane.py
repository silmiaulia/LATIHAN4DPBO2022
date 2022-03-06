
# Saya Silmi Aulia Rohmah mengerjakan Latihan 4 DPBO 2022 C1 
# dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan 
# kecurangan seperti yang telah dispesifikasikan. Aamiin 

from Vehicle import Vehicle

class Airplane(Vehicle):

    
    def __init__(self): #Constructor

        self.wingsLength = 0
        self.airlines = ""
        self.cost = 0

    # metode getter dan setter
    def getWingsLength(self):
        return self.wingsLength
    
    def setWingsLength(self, wingsLength):
        self.wingsLength = wingsLength

    def getAirlines(self):
        return self.airlines
    
    def setAirlines(self, airlines):
        self.airlines = airlines

    def getCost(self):
        return self.cost
    
    def setCost(self, cost):
        self.cost = cost

    # prosedur untuk print informasi class
    def getAirplane(self):
        
        print("Airlines           : " + self.getAirlines())
        print("Wings Length       : " + str(self.getWingsLength()) + " meter")
        print("Aircraft Cost      : " + str(self.getCost()) + " Million U.S dollars")
        print()