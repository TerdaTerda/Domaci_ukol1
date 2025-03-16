#Pokoušela jsem se o všechny bonusy

from math import ceil
from abc import ABC, abstractmethod
from enum import Enum

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

manetin = Locality("Manětín", 0.8)
brno = Locality("Brno", 3)

class Property_type(Enum):
    land = 1
    building_site = 2
    forrest = 3
    garden = 4

class Property(ABC):
    def __init__(self, name, locality:Locality):
        self.locality = locality
        self.name = name

class Estate(Property):
    def __init__(self, name, locality, estate_type: Property_type, area):
        super().__init__(name, locality)
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):
        if self.estate_type == Property_type(1):
            estate_coefficient = 0.85

        elif self.estate_type == Property_type(2):
            estate_coefficient = 9

        elif self.estate_type == Property_type(3):
            estate_coefficient = 0.35

        elif self.estate_type == Property_type(4):
            estate_coefficient = 2

        else:
            return f"Please select valid estate type: land, building site, forrest or garden."
        
        tax = ceil(self.area * estate_coefficient * self.locality.locality_coefficient)
        return tax
    
    def __str__(self):
        return f"{self.name}, lokalita {self.locality.name}, {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."

class Residence(Property):
    def __init__(self, name, locality, area, commercial: bool):
        super().__init__(name, locality)
        self.area = area
        self.commercial = commercial
    
    def calculate_tax(self):
        if self.commercial == True:
            tax = ceil(self.area * self.locality.locality_coefficient * 15 * 2)
        else:
            tax = ceil(self.area * self.locality.locality_coefficient * 15)
        return tax

    def __str__(self):
        return f"{self.name}, lokalita {self.locality.name}, {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."

class TaxReport:
    def __init__(self, name,):
        self.name = name
        self.property_list = []

    def add_property(self, objekt):
        self.property_list.append(objekt)
    
    def calculate_tax(self):
        total_tax = 0
        for property in self.property_list:
            total_tax = total_tax + property.calculate_tax()

        return f"Celková daň z nemovitostí je {total_tax}."

zemedelsky_pozemek = Estate("Zemědělský pozemek",manetin, Property_type(1),900)
dum_s_podlahovou_plochou = Residence("Dům s podlahovou plochou",manetin, 120, False)
kancelar = Residence("Kancelář",brno, 90, True)

print(zemedelsky_pozemek)
print(dum_s_podlahovou_plochou)
print(kancelar)

report_1 = TaxReport("Tereza Sadilová")

report_1.add_property(zemedelsky_pozemek)
report_1.add_property(dum_s_podlahovou_plochou)

print(report_1.calculate_tax())


