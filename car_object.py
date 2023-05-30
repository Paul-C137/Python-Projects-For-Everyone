# create a class constructor and define the attributes and methods
class Car:
    def __init__(self, color='red', size='compact', year=2020):
        self.color = color
        self.size = size
        self.year = year
        # notice no default is set for the 'make' attribute
        self.make = ''
    
    # the "set" methods allow us to change the attributes
    def set_color(self, color):
        self.color = color

    # the "get" methods allow us to access the value of attributes
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
    
    def set_make(self, make):
        self.make = make

    # some methods allow us to perform actions
    def drive_forward(self):
        # replace this with actual logic to move x and y position
        # of course x and y positions would have to be attributes 
        # of the object defined above
        # then, you could "drive forward"
        print("Car is driving forward.")

    def drive_backward(self):
        # put the logic for driving backward here
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

    car1.set_make('DeLorean')
    print(car1.make)


if __name__ == "__main__":
    main()
