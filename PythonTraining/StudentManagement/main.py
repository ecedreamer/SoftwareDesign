import sqlite3


def get_sqlite_connection():
    database_path = "student_mgmt.db"
    connection = sqlite3.connect(database_path)
    return connection


def create_table():
    con = get_sqlite_connection()
    con.execute("""
                CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL, batch TEXT NOT NULL, address TEXT NOT NULL, date_of_birth TEXT NOT NULL, mobile TEXT)
                """)
    con.commit()
    con.close()


def get_student_list():
    con = get_sqlite_connection()
    cursor = con.execute("Select * from students")
    student_list = cursor.fetchall()
    cursor.close()
    return student_list


def get_student(student_id):
    student = None
    return student


def insert_student(name, email, batch, address, date_of_birth, mobile=None):
    con = get_sqlite_connection()
    con.execute("""
            INSERT INTO students(name, email, batch, address, date_of_birth, mobile) VALUES(?, ?, ?, ?, ?, ?)
            """, (name, email, batch, address, date_of_birth, mobile))
    con.commit()
    con.close()
    student_id = None
    return student_id


def update_student(student_id, name=None, email=None, batch=None, address=None, date_of_birth=None, mobile=None):
    updated_student = None
    return updated_student


def delete_student(student_id):
    is_deleted = False
    return is_deleted



def main():
    create_table()
    print("Student Record Management System running...")

    print("press 'l' for all students")
    print("press 'g' for single student")
    print("press 'i' for adding a student")
    print("press 'u' for updating a student")
    print("press 'd' for deleting a student")
    print("press 'q' for quiting the application")
    # infinite loop to make a service
    while True:
        user_input = input("Choose your option: ").lower()
        if user_input == "l":
            result = get_student_list()
            for student in result:
                print(student)
        elif user_input == "g":
            ...
        elif user_input == "i":
            print("Field marked with * are mandatory")
            s_name = input("Enter name *: ")
            s_email = input("Enter email *: ")
            s_batch = input("Enter batch *: ")
            s_address = input("Enter address *: ")
            s_dob = input("Enter DOB *: ")
            s_mobile = input("Enter mobile(Optional): ")
            inserted_id = insert_student(s_name, s_email, s_batch, s_address, s_dob, s_mobile)
            print(inserted_id)
        elif user_input == "u":
            ...
        elif user_input == "d":
            ...
        elif user_input == "q":
            ...
        else:
            print("Your input is invalid. Please choose again: ")


if __name__ == "__main__":
    main()