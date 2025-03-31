class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year
        self.__mileage = 0

    @property
    def miles(self):
        return self.__mileage

    @miles.setter
    def miles(self, miles):
        if miles < 0:
            raise ValueError("Miles cannot be less than 0")
        self.__mileage = miles

cars = []

def main():
    try:
        make = input("Make: ")
        model = input("Model: ")
        year = int(input("Year: "))
        mileage = int(input("Miles: "))
    except ValueError:
        print("Positive whole numbers only.")
    
    new_car = Car(make, model, year)
    new_car.miles = mileage
    cars.append(new_car)

    print(f"{new_car.make} | {new_car.model} | {new_car.year} | {new_car.miles}")
    

if __name__ == "__main__":
    main()
