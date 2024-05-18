data_types = [
    "int",
    "float",
    "boolean",
    "None", 


    "string",
    "list", 
    "tuple", 
    "set", 
    "dictionary"
]

is_passed = True
is_passed = False
passed_students = None
failed_students = ["Simon", "Pawan", "Atom", 323, 45.5, True, ["dipak", "hi"], "Simon"]
week_days = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat") # tuple
eaten_fruits = {"apple", "orange", "banana"} # set

students_info = {
    "name": "Dipak Niroula",
    "roll": 32,
    "mobile": ["8998989898", "989898989"],
    "gender": "male",
    "has_registered": False,
    "interests": {
        "game": "Football",
        "study": "science"
    }
}

print(students_info["interests"])