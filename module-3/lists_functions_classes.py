class Vehicle:
    def __init__(self, vehicle_type="car"):
        self.vehicle_type = vehicle_type

    def __str__(self):
        return f"Vehicle type: {self.vehicle_type}"


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        return f"""{super().__str__()}
Year: {self.year}
Make: {self.make}
Model: {self.model}
Number of doors: {self.doors}
Type of roof: {self.roof}"""


my_car = Automobile("car", 2020, "Toyota", "Corolla", 4, "sun roof")
print(my_car)

print("Welcome to the vehicle configurator! Type in your vehicle information below.")
vehicle_year = input("What year is the vehicle? ")
vehicle_make = input("What is the make of the vehicle? ")
vehicle_model = input("What is the vehicle model? ")

while True:
    vehicle_number_of_doors = input(
        "How many doors does the vehicle have (e.g. 2 or 4)? "
    )
    if vehicle_number_of_doors in ["2", "4"]:
        break
    else:
        print("Unknown number of doors! Please try again using either 2 or 4.")

while True:
    vehicle_roof_type = input(
        "What kind of roof does the vehicle have (e.g. 'sun roof' or 'solid')? "
    )
    if vehicle_roof_type in ["sun roof", "solid"]:
        break
    else:
        print("Unknown roof type! Please try again using either 'sun roof' or 'solid'.")

your_car = Automobile(
    "car",
    vehicle_year,
    vehicle_make,
    vehicle_model,
    vehicle_number_of_doors,
    vehicle_roof_type,
)

print(your_car)
