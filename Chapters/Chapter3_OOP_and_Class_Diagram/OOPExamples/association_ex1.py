"""
Association: Association is a relationship among objects where one object is associated with other type of object. It has weeker relationship since the related objects have separate existance or lifetime. It is also one of the fundamental concepts of OOP. 

Example: Student object has a Laptop object. But Student object is not composed of the Laptop object.
"""


class Student:
    def __init__(self, name: str, student_id, email, program, batch):
        self.name = name
        self.student_id = student_id
        self.student_email = email
        self.program = program
        self.batch = batch

    def get_student_intro(self):
        return self.program + "-" + str(self.batch) + "; " + self.name + "_" + str(self.student_id)
    
class Laptop:
    def __init__(self, brand: str, model: str, owner: Student): # type hint
        self.brand = brand
        self.model = model
        self.owner = owner

    def get_laptop_info(self):
        return self.brand + "-" + self.model
    
    def get_owner_info(self):
        return self.owner.get_student_intro()
    

def main():
    student1 = Student("Prabin Babu Kattel", 1003, "babu@gmail.com", "AI", 36)
    student2 = Student("Rohit Shah", 1006, "rohit@gmail.com", "AI", 36)
    laptop1 = Laptop("Lenovo", "Legion 5", owner=student2)
    laptop2 = Laptop("Asus", "G16", student1)
    laptop3 = Laptop("Asus", "Purano", student2)

    # intro = student1.get_student_intro()
    # print(intro)

    laptop_info = laptop1.get_laptop_info()
    print(laptop_info)
    print(laptop1.get_owner_info())

    laptop_info = laptop2.get_laptop_info()
    print(laptop_info)
    print(laptop2.get_owner_info())
    


main()

""" OUTPUT
Lenovo-Legion 5
AI-36; Rohit Shah_1006
Asus-G16
AI-36; Prabin Babu Kattel_1003
"""





        