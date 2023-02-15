class Vehicle():
    def __init__(self, owner, brand, model, price, years_driven):
        self.owner = owner
        self.brand = brand
        self.model = model
        self.price = price
        self.years_driven = years_driven


owner1 = Vehicle("Swabir", "BMW", "X5", "12M", "5 years")
print(owner1.owner)
print(owner1.brand)
print(owner1.model)
print(owner1.price)
print(owner1.years_driven)

print("----End of owner1------")


owner2 = Vehicle("Maundu", "Mercedes", "C 200", "9M", "3 years")
print(owner2.owner)
print(owner2.brand)
print(owner2.model)
print(owner2.price)
print(owner2.years_driven)

print("----End of owner2------")

owner3 = Vehicle("Nelson", "Nissan", "GTR", "19M", "6 years")
print(owner3.owner)
print(owner3.brand)
print(owner3.model)
print(owner3.price)
print(owner3.years_driven)
