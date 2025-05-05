class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee

# Usage
emp = Employee("Alishba")
dept = Department(emp)
print("Department Employee:", dept.employee.name)
