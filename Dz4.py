print('Task1-st')

class Person:
    def Healthquality(self, punchesinsek, Brainwawes):
        self.punchesinsek = punchesinsek
        self.brainwaves = Brainwawes
    def display_info(self):
        print('from this person', self.punchesinsek, 'punches in second')
        print('from this person', self.brainwaves, )
print(10, 55)
print('Task 2-nd')
class Temp:
    def c_to_fr(self,c,f):
        self.c=c
        self.f=f
    def display_info(self):
          print ('Farengeyt is: ', (self.c * 9)/5 + 32)
          print ('Celsium is:',(self.f-32)*5/9)

day_one = Temp('30','55')
day_one.display_info()