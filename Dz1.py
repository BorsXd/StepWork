class Car:
    def __init__(self, mark, motor, horsestrenght, fuel):
        self.mark = mark
        self.motor = motor
        self.horsestrenght = horsestrenght
        self.fuel = fuel
    def display_info(self):
        print('Mark is: ', self.mark)
        print('Motor is: ', self.motor)
        print('Horsestrenght is: ', self.horsestrenght)
        print('Fuel is: ', self.fuel)
car1 = Car('Bmw','t-44', 55,'44 litr' )
car1.display_info()
car2 = Car('toyota', 'd-56', '90', '')
car2.display_info()