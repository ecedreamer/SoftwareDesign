# Encapsulation: wrapping of data | attributes | property and methods | behavior of objects into a single class is called encapsulation. Only the object of a class can access them. 

class Teacher:
    def set_name(self, name):
        self.full_name = name


class Student:
    def set_email(self, email):
        self.student_email = email

    def get_email(self):
        return self.student_email



t1 = Teacher()
t2 = Teacher()
t1.set_name("DIpak Niroula")
t2.set_name("Dikshant Thakuri")

print(t2.full_name)


s1 = Student()

s1.set_email("sangit.niroula@gmail.com")
email = s1.get_email()
print(email, "-------")