
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


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Byron', 'Martienz', 50000, 'Python')
dev_2 = Developer('Yolanda', 'Martienz', 60000, 'java')

mgr_1 = Manager('Nanigi', 'Martinez', 90000, [dev_1])

print(issubclass(Developer, Manager))
# print(mgr_1.email)
# mgr_1.remove_emp(dev_1)
# mgr_1.add_emp(dev_2)

# mgr_1.print_emps()

# print(dev_1.email)
# print(dev_2.email)

# print(dev_1.email)
# print(dev_2.prog_lang)
