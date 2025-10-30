class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init_(self):
        super().__init__( name, age)
    def show_student(self):
        print("Name:",self.name)
        print("Age:",self.age)



new_person=Student("anu",19)
new_person.show_student()