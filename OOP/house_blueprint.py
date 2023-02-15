class House():
    def __init__(self, location, owner, price, roof):
        self.location = location
        self.owner = owner
        self.price = price
        self.roof = roof


house_owner1 = House("Westlands", "Swabir", "6.5M", "98")
print(house_owner1.location)
print(house_owner1.owner)
print(house_owner1.price)
print(house_owner1.roof)

print("-----End of owner 1-------")

house_owner2 = House("Ngara", "Kadish", "7M", "120")
print(house_owner2.location)
print(house_owner2.owner)
print(house_owner2.price)
print(house_owner2.roof)