class details_fo(object):
  def __init__(self, id, name, description):
    self.id = id
    self.name = name
    self.description = description

  def alter(self, id, name = None, description = None):
    self.id = id
    if name != None:
        self.name = name
    if description != None:
        self.description = description

  def __str__(self):
    return f'{self.id} {self.name} : {self.description}'

s =  details_fo(101, 'Jeline', 'Senior Associate')
print(s)
s.alter(101, 'Faitus Jeline', 'Senior Associate - Projects')
print(s)
s.alter(110)
print(s)
s.alter(101, 'Faitus Jeline Joseph')
print(s)
