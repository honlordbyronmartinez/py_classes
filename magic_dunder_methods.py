
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


dev_1 = Employee('Byron', 'Martienz', 50000, 'Python')
dev_2 = Employee('Yolanda', 'Martienz', 60000, 'java')
