
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

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first,
                                                   self.last,
                                                   self.pay
                                                   )

    def __str__(self):
        return '{} - {}'.format(self.first,
                                self.last
                                )

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


dev_1 = Employee('Byron', 'Martienz', 50000)
dev_2 = Employee('Yolanda', 'Martienz', 60000)

# print(dev_1)
# print(repr(dev_1))
# # print(str(dev_1))
#
# print(dev_1 + dev_2)

print(len(dev_1))
