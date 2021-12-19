
class Family(object):
    """Describe a family"""
    family_name = ''

    def __init__(self, f_name=''):
        self.family_name = f_name
pass


class Child1(Family):
    """Describe a child"""
    first_name = ''

    def __init__(self, f_name='', first_name=''):
        super().__init__(f_name)
        self.first_name = first_name

    def print_child_details(self):
        print('Child { first name: ' + self.first_name + ', last name: ' + self.family_name + ' }')
pass


class Child2(Family):
    """Describe a child"""
    first_name = ''

    def __init__(self, f_name='', first_name=''):
        super().__init__(f_name)
        self.first_name = first_name

    def print_child_details(self):
        print('Child { first name: ' + self.first_name + ', last name: ' + self.family_name + ' }')

pass

child1 = Child1('Noiman', 'Sara1')
child1.print_child_details()

child2 = Child2(child1.family_name, 'Sara2')
child2.print_child_details()