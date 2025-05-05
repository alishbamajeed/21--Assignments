class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          
        self._salary = salary    
        self.__ssn = ssn         


emp = Employee("Alishba", 800000, "123-45-6789")


print(f"Name: {emp.name}")


print(f"Salary: {emp._salary}")

print(f"SSN (using name mangling): {emp._Employee__ssn}")
