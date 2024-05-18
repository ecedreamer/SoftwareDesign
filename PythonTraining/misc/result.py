science_marks = int(input("Enter your science marks: "))
math_marks = int(input("Enter your math marks: "))
nepali_marks = int(input("Enter your nepali marks: "))

average = (science_marks + math_marks + nepali_marks) / 3


if average < 50 or science_marks < 50 or math_marks < 50 or nepali_marks < 50:
    print("You are fail")
elif average >= 50 and average < 60:
    print("Third division")
elif average >= 60 and average < 80:
    print("Second division")
elif average >= 80 and average < 90:
    print("First division")
elif average >= 90:
    print("Distinction")