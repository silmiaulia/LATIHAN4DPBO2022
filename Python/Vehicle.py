
# Saya Silmi Aulia Rohmah mengerjakan Latihan 4 DPBO 2022 C1 
# dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan 
# kecurangan seperti yang telah dispesifikasikan. Aamiin 

class Vehicle:

    def __init__(self): #Constructor

        self.VehicleName = ""
        self.type = ""
        self.age = 0
        self.fuelType = ""
        self.maxPassengers = 0

    # metode getter dan setter
    def getVehicleName(self):
        return self.VehicleName
    
    def setVehicleName(self, VehicleName):
        self.VehicleName = VehicleName

    def getType(self):
        return self.type
    
    def setType(self, type):
        self.type = type

    def getAge(self):
        return self.age
    
    def setAge(self, age):
        self.age = age

    def getfuelType(self):
        return self.fuelType
    
    def setfuelType(self, fuelType):
        self.fuelType = fuelType

    def getmaxPassengers(self):
        return self.maxPassengers
    
    def setmaxPassengers(self, maxPassengers):
        self.maxPassengers = maxPassengers

    # prosedur move
    def move(self): 

        print("This " + self.getVehicleName() + " is moving..")

    # prosedur untuk print informasi class
    def getVehicle(self):
        
        self.move()
        print("Type               : " + self.getType())
        print("Age                : " + str(self.getAge()) + " Tahun")
        print("Fuel Type          : " + self.getfuelType())
        print("Maximum Passengers : " + str(self.getmaxPassengers()) + " Orang")
        
        

