
# Saya Silmi Aulia Rohmah mengerjakan Latihan 4 DPBO 2022 C1 
# dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan 
# kecurangan seperti yang telah dispesifikasikan. Aamiin 

from Person import Person
from Job import Job
from Vehicle import Vehicle


class Driver(Person, Job):

    def __init__(self): #Constructor

        self.lisenceID = ""
        self.activeUntil = 0
        self.vehicleType = ""
        self.vehicle = Vehicle() # composition
        

    # metode getter dan setter
    def getLisenceID(self):
        return self.lisenceID
    
    def setLisenceID(self, lisenceID):
        self.lisenceID = lisenceID

    def getActiveUntil(self):
        return self.activeUntil
    
    def setActiveUntil(self, activeUntil):
        self.activeUntil = activeUntil

    def getVehicleType(self):
        return self.vehicleType
    
    def setVehicleType(self, vehicleType):

        self.vehicleType = vehicleType

    def getVehicle(self):
        return self.vehicle
    
    def setVehicle(self, vehicle):

        self.vehicle = vehicle


    # prosedur untuk print informasi class
    def getDriver(self):

        print("Lisence ID     : " + self.getLisenceID())
        print("Active Until   : " + str(self.getActiveUntil()))
        print("---------------------------------------")

        if(self.getVehicleType() == "Airplane"):
            print("This person drives an " + self.getVehicleType())
           
        elif(self.getVehicleType() == "Ship"):
            print("This person drives a " + self.getVehicleType())
   
        print("---------------------------------------")

        self.vehicle.getVehicle()