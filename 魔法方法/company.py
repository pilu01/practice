

class Company():
    def __init__(self, employee_list):
        self.employee = employee_list

    # item 类似位置信息
    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

    def __str__(self):
        return ','.join(self.employee)


company = Company(['tom', 'bob', 'jane'])

print(company)


