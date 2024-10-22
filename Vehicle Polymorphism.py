class Ferrari:
    def fuel_type(self):
        print("Fuel type of Ferrari is Petrol")
        
    def max_speed(self):
        print("Max Speed of Ferarri is 350")
        
        print()
        
class BMW:
    def fuel_type(self):
        print("Fuel type of BMW is Diesel")
        
    def max_speed(self):
        print("Max speed of BMW is 250")
        
        print()
        
class Lambu:
    def fuel_type(self):
        print("Fuel type of lambu is Petrol")
    
    def max_speed(self):
        print("Max speed of lambu is 350")
        
        print()
        
class Nissan:
    def fuel_type(self):
        print("Fuel type of Nissan is unleaded gasoline,")
        
        
        
    def max_speed(self):
        print("Max speed of Nissan is 480")
        
        print()
        
class Volkswagen:
    def fuel_type(self): 
        print("Fuel type of Volkswagen is regular unleaded gas")
    
    def max_speed(self):
        print("Max speed of Volkswagen is 155")
        
        print()
        
        
ferrari  = Ferrari()
bmw = BMW()
lambu = Lambu()
nissan = Nissan()
volkswagen = Volkswagen()

for car in (ferrari,bmw,lambu,nissan,volkswagen):
    
    car.fuel_type()
    car.max_speed()