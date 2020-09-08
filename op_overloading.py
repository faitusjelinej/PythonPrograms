class Properties(object):
    def __init__(self,props):
        self.props = []
        if type(props) in (list, tuple):
            self.props.extend(props)


    def __add__(self, other):
        return Properties(self.props + other.props)

    def __sub__(self, other):
        return Properties([p for p in self.props if p not in other.props])

    def __str__(self):
        return f'Content : {self.props}'

p1 = Properties(('a','b','c'))
p2 = Properties(['d','e'])
p3 = Properties(['a','d'])


print('p1 :' + str(p1))
print('p2 :' + str(p2))
print('p3 :' + str(p3))

p4 = p1 + p2
print('p4 :' + str(p4))

p5 = p4 - p3
print('p4 - p3:' + str(p5))
