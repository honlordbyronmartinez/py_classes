# Python Object-Oriented Programming


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pya = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Byron', 'Martienz', 50000)
emp_2 = Employee('Yolanda', 'Martienz', 60000)

print(Employee.fullname(emp_2))
print(emp_2.fullname())
