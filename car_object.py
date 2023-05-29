class Car:
    def __init__(self, color='red', size='compact', year=2020):
        self.color = color
        self.size = size
        self.year = year

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def drive_forward(self):
        print("Car is driving forward.")

    def drive_backward(self):
        print("Car is driving backward.")


def main():
    # Create a car object with default attributes
    car1 = Car()
    print(f"Default color: {car1.get_color()}")
    print(f"Default size: {car1.get_size()}")
    print(f"Default year: {car1.get_year()}")

    # Set new attributes using the setter methods
    car1.set_color('blue')
    car1.set_size('sedan')
    car1.set_year(2022)

    # Get and print the updated attributes using the getter methods
    print(f"Updated color: {car1.get_color()}")
    print(f"Updated size: {car1.get_size()}")
    print(f"Updated year: {car1.get_year()}")

    # Drive the car forward and backward
    car1.drive_forward()
    car1.drive_backward()


if __name__ == "__main__":
    main()
