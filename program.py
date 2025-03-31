class Car:
    def __init__(self, make: str, model: str, year: int, color: str):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.__mileage = 0

    @property
    def miles(self):
        """Getter for mileage."""
        return self.__mileage

    @miles.setter
    def miles(self, miles):
        """Setter for mileage."""
        if miles < 0:
            raise ValueError("Miles cannot be less than 0")
        self.__mileage = miles

cars = []

def main():
    while True:
        try:
            make = input("Make: ").title().strip()

            model = input("Model: ").title().strip()

            year = int(input("Year: ").strip())
            if year < 1800 or year > 2026:
                raise Exception("Impossible year!")
            
            color = input("Color: ").lower().strip()

            mileage = int(input("Miles: ").strip())
            break
        except ValueError:
            print("Positive whole numbers only.")
    
    new_car = Car(make, model, year, color)
    new_car.miles = mileage

    cars.append(new_car)
    print(f"{new_car.make} | {new_car.model} | {new_car.year} | {new_car.color} | {new_car.miles}")
    

if __name__ == "__main__":
    main()

# getter and setter name must be the same
# Private variable doesn't go in class parameters

# When you call them, setter has an '=' after, while getter is just mentioned.
# ex. new_car.miles = 300 (setter), new_car.miles (getter)