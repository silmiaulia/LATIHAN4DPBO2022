
# Saya Silmi Aulia Rohmah mengerjakan Latihan 4 DPBO 2022 C1 
# dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan 
# kecurangan seperti yang telah dispesifikasikan. Aamiin 

# import kelas
from Vehicle import Vehicle
from Ship import Ship
from Airplane import Airplane
from Person import Person
from Job import Job
from Driver import Driver

# 1st Person -----------
pengemudi1 = Driver()
pengemudi1.setNik("200031988010")
pengemudi1.setName("Selly Aggraeni")
pengemudi1.setGender("Perempuan")
pengemudi1.setNIP("199201756")
pengemudi1.setCompanyName("PT Garuda Indonesia")
pengemudi1.setPosition("Pilot")
pengemudi1.setLisenceID("999100")
pengemudi1.setActiveUntil(2025)
pengemudi1.setVehicleType("Airplane")

v1 = Airplane()
v1.setVehicleName("Airplane")
v1.setType("Boeing")
v1.setAge(20)
v1.setfuelType("Aviation gasolines")
v1.setmaxPassengers(230)
v1.setWingsLength(40)
v1.setAirlines("Garuda")
v1.setCost(99.7)

pengemudi1.setVehicle(v1)

print("=======================================")
print("      First Person Information")
print("=======================================")

pengemudi1.getPersons()
pengemudi1.getJob()
pengemudi1.getDriver()
v1.getAirplane()


# 2nd Person -------------

pengemudi2 = Driver()
pengemudi2.setNik("231092840290")
pengemudi2.setName("Deril Ilham")
pengemudi2.setGender("Laki-laki")
pengemudi2.setNIP("192020001")
pengemudi2.setCompanyName("A.P. Moller Maersk Group")
pengemudi2.setPosition("Helmsman")
pengemudi2.setLisenceID("8782653535")
pengemudi2.setActiveUntil(20022)
pengemudi2.setVehicleType("Ship")

v2 = Ship()
v2.setVehicleName("Ship")
v2.setType("Container Ships")
v2.setAge(35)
v2.setfuelType("Methanol")
v2.setmaxPassengers(30)
v2.setCountryOfManufacture("Denmark")
v2.setSpeed(27.6)
v2.setGrossTonnage(170.794)

pengemudi2.setVehicle(v2)

print("=======================================")
print("      Second Person Information")
print("=======================================")

pengemudi2.getPersons()
pengemudi2.getJob()
pengemudi2.getDriver()
v2.getShip()


# 3rd Person ----------------

pengemudi3 = Driver()
pengemudi3.setNik("499029393203")
pengemudi3.setName("Chris P")
pengemudi3.setGender("Laki-laki")
pengemudi3.setNIP("1990287364")
pengemudi3.setCompanyName("Euronav NV")
pengemudi3.setPosition("Helmsman")
pengemudi3.setLisenceID("29109221")
pengemudi3.setActiveUntil(2031)
pengemudi3.setVehicleType("Ship")

v3 = Ship()
v3.setVehicleName("Ship")
v3.setType("Supertankers Ships")
v3.setAge(19)
v3.setfuelType("Bunker fuel")
v3.setmaxPassengers(50)
v3.setCountryOfManufacture("South Korea")
v3.setSpeed(18.9)
v3.setGrossTonnage(2.12)

pengemudi3.setVehicle(v3)

print("=======================================")
print("      Third Person Information")
print("=======================================")

pengemudi3.getPersons()
pengemudi3.getJob()
pengemudi3.getDriver()
v3.getShip()

# 4th Person ---------

pengemudi4 = Driver()
pengemudi4.setNik("398238290923920")
pengemudi4.setName("Ariel Hakim")
pengemudi4.setGender("Laki-laki")
pengemudi4.setNIP("1998210920")
pengemudi4.setCompanyName("Lockheed Martin Corporation")
pengemudi4.setPosition("Pilot")
pengemudi4.setLisenceID("78877474")
pengemudi4.setActiveUntil(20024)
pengemudi4.setVehicleType("Airplane")

v4 = Airplane()
v4.setVehicleName("Airplane")
v4.setType("Jets")
v4.setAge(20)
v4.setfuelType("Kerosene")
v4.setmaxPassengers(19)
v4.setWingsLength(10.7)
v4.setAirlines("Lockheed Martin")
v4.setCost(78)

pengemudi4.setVehicle(v4)

print("=======================================")
print("      Fourth Person Information")
print("=======================================")

pengemudi4.getPersons()
pengemudi4.getJob()
pengemudi4.getDriver()
v4.getAirplane()

# 5th Person -------------

pengemudi5 = Driver()
pengemudi5.setNik("5010928730299392")
pengemudi5.setName("Dania Rahayu")
pengemudi5.setGender("Perempuan")
pengemudi5.setNIP("1920193823820")
pengemudi5.setCompanyName("Airbus")
pengemudi5.setPosition("Pilot")
pengemudi5.setLisenceID("19288282")
pengemudi5.setActiveUntil(20027)
pengemudi5.setVehicleType("Airplane")

v5 = Airplane()
v5.setVehicleName("Airplane")
v5.setType("Cargo")
v5.setAge(12)
v5.setfuelType("Jet A-1")
v5.setmaxPassengers(4)
v5.setWingsLength(44.84)
v5.setAirlines("Airbus")
v5.setCost(44)

pengemudi5.setVehicle(v5)

print("=======================================")
print("      Fifth Person Information")
print("=======================================")

pengemudi5.getPersons()
pengemudi5.getJob
pengemudi5.getDriver()
v5.getAirplane()


