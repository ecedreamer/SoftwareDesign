
class Student:
    def __init__(self, name, email, roll_no): # initializer method
        self.full_name = name # assigning value to attributes
        self.email = email
        self.roll = roll_no

    def take_attendance(self): # method
        print("My roll no is ", self.roll)

    def submit_assignment(self): # method
        print("Assignment submitted successfully")

    def play_game(self, game_name): # method
        print("I played", game_name, "game with friends")

    def get_email(self): # method
        return self.email

    
s1 = Student("Dipak", "dipak@gmail.com", "10")
s1.take_attendance()
s2 = Student("Rohit", "rohit@gmail.com", 1)
s2.take_attendance()
s2.play_game("Chess")