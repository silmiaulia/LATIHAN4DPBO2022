# LATIHAN4DPBO2022

> Saya Silmi Aulia Rohmah mengerjakan Latihan 3 DPBO 2022 C1 dalam mata kuliah DPBO untuk keberkahanNya 
> maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin 

### Deskripsi Program 
Terdapat enam kelas yang ada pada program latihan 4 ini. Pada projek ini setiap tiga kelas dibagi menjadi dua hubungan yaitu **Multiple Inheritance** dan **Hierarchical Inheritance**. Kelas Driver, Person, dan Job memiliki hubungan multiple inheritance, dimana kelas Persons dan Job menjadi parent dari kelas driver. Alasannya karena dalam kehidupan nyata pun seorang driver merupakan orang dan juga sebuah pekerjaan maka kelas Driver memiliki hubungan *is a* dengan kedua kelas parents nya. Sedangkan kelas Vehicle diwariskan kepada kelas Ship dan Airplane, karena Airplane dan juga Ship merupakan sebuah Vehicle.Maka dari itu ketiganya memiliki hubungan *is a* dengan bentuk hierarchical inheritance. Kemudian kelas Driver dan Vehicle juga dihubungkan dengan hubungan **Composition**, karena diasumsikan seorang driver memiliki sebuah vehicles.

#### Link Desain Program : https://drive.google.com/file/d/1kUjpUhARZMfvNTSeg3Kupizth-P88RmC/view?usp=sharing
<p align="center">
  <img width="707" height="542" src="https://github.com/silmiaulia/LATIHAN4DPBO2022/blob/main/Desain%20Program.png?raw=true">
</p>

Terdapat perubahan atribut pada kelas Vehicle, Ship, dan Airplane yaitu atribut age dan type dihilangkan dari kelas Ship dan Airplane dan dipindahkan kepada parentnya yaitu kelas Vehicle. Kemudian terdapat penambahan atribut baru pada kelas Ship dan Airplane. Berikut ini secara lebih jelasnya data atribut pada setiap kelas

1. Vehicle
   - VehicleName
   - type
   - age
   - fuelType
   - maxPassengers
2. Ship
   - countryOfManufacture
   - speed
   - grossTonnage
3. Airplane
   - wingsLength
   - airlines
   - cost
4. Person
   - Nik
   - Name
   - Gender
5. Job
   - Nip
   - companyName
   - posiyion
6. Driver
   - lisenceID
   - activeUntil
   - vehicleType
   - Vehicle


### Screenshot Program

<p align="left">
  <img width="543" height="552" src="https://github.com/silmiaulia/LATIHAN4DPBO2022/blob/main/Screenshot/1.png?raw=true">
</p>

<p align="left">
  <img width="543" height="552" src="https://github.com/silmiaulia/LATIHAN4DPBO2022/blob/main/Screenshot/2.png?raw=true">
</p>

<p align="left">
  <img width="652" height="353" src="https://github.com/silmiaulia/LATIHAN4DPBO2022/blob/main/Screenshot/3.png?raw=true">
</p>
