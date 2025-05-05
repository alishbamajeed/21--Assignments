class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
       
        super().__init__(name)
        self.subject = subject

teacher = Teacher("Alishba", "Science")


print(f"Teacher Name: {teacher.name}")
print(f"Subject: {teacher.subject}")
