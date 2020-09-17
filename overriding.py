class Employee:
  def setworkinghours(self):
    self.workinghours = 40

  def dispayworkinghours(self):
    print(self.workinghours)

class Trainee(Employee):
  def setworkinghours(self):
    self.workinghours = 45 #overridding

  def resetworkinghours(self):
    super().setworkinghours()

employee = Employee()
employee.setworkinghours()
print("Number of working hours of the empoyee is",end = ' ')
employee.dispayworkinghours()
trainee = Trainee()
trainee.setworkinghours()
print("Number of working hours of the trainee is",end = ' ')
trainee.dispayworkinghours()

trainee.resetworkinghours()
print("Number of working hours of the trainee after reset",end = ' ')
trainee.dispayworkinghours()
