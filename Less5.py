class Human:
    def __init__(self, name):
        self.name = name
class Auto:
    def __init__(self, brand):
        self.brand=brand
        self.passengers = []
    def add_passenger(self,human):
        self.passengers.append(human)
    def print_passengers_names(self):
        if passengers != []:
            print(f'Names of{self.brand} car passengers')
            for i  in self.passengers:
                print(i.name)
        else:
            print(f"There're no passengers in {self.brand}, car ")
artur = Human('Artur')
john = Human('John')
aziz = Human('Aziz')
car  = Auto(input())
car.add_passenger(artur)
car.add_passenger(john)
car.add_passenger(aziz)
car.print_passengers_names()





passengers = ['Johny', 'Hitler', 'Ilyu', 'Vagif']
passengers.append('Putlya')
print(passengers)
for i in passengers:
    print(i)