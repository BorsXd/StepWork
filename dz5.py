class numbers:
    def __init__(self, number1, number2, number3, number4):
        self.num1 = number1
        self.num2 = number2
        self.num3 = number3
        self.num4 = number4
    def formula(self):
        print((self.num1+self.num2+self.num3+self.num4)/4)
        if self.num1 > self.num2 > self.num3 > self.num4:
            print(self.num1)
        elif self.num2 > self.num1 > self.num3 > self.num4:
            print(self.num2)
        elif self.num3 > self.num2 > self.num1 > self.num4:
            print(self.num3)
        elif self.num4 > self.num2 > self.num3 > self.num1:
            print(self.num4)

numberkit1 = numbers(55, 66, 33, 22)
numberkit1.formula()
numberkit2 = numbers(55, 44, 77, 22)
numberkit2.formula()
print('Task 2')
class person:
    def __init__(self, name):
        self.name = name
class health_quality:
  def __init__(self,heartpunch, breathinsec):
      self.hearpun = heartpunch
      self.breasec = breathinsec
      self.medic = []
  def add_medic(self,person):
      self.medic.append(person)
  def print_medic_names(self):
      if self.medic != []:
          print('heart punch is', self.hearpun, 'punches in second')
          print('breathing is', self.breasec, 'inhales in second')


aziz = person("Aziz")
aziz1 = health_quality(55, 66)
aziz1.add_medic(aziz)
aziz1.print_medic_names()





