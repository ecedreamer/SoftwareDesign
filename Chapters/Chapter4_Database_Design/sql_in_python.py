import sqlite3

# Function to create tables
def create_tables():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    
    # Creating batch table
    c.execute('''CREATE TABLE IF NOT EXISTS batch (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    batch_name TEXT NOT NULL,
                    start_date TEXT,
                    end_date TEXT
                )''')

    # Creating student table
    c.execute('''CREATE TABLE IF NOT EXISTS student (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    address TEXT,
                    batch_id INTEGER NOT NULL,
                    FOREIGN KEY (batch_id) REFERENCES batch(id)
                )''')

    conn.commit()
    conn.close()

# Function to insert data
def insert_data():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    
    # Inserting batches
    batches = [('AI-36', '2024-01-01', '2027-01-01'),
               ('CS-36', '2024-01-01', '2027-01-01')]
    c.executemany('INSERT INTO batch (batch_name, start_date, end_date) VALUES (?, ?, ?)', batches)
    
    # Inserting students
    students = [('Student 1', 'student1@example.com', 'Address 1', 1),
                ('Student 2', 'student2@example.com', 'Address 2', 1),
                ('Student 3', 'student3@example.com', 'Address 3', 1),
                ('Student 4', 'student4@example.com', 'Address 4', 2),
                ('Student 5', 'student5@example.com', 'Address 5', 2),
                ('Dipak Niroula', 'dipak@example.com', 'Satdobato', 1),
                ('Rupak Kafle', 'rupak@example.com', 'Bhaktapur', 2)]
    c.executemany('INSERT INTO student (name, email, address, batch_id) VALUES (?, ?, ?, ?)', students)

    conn.commit()
    conn.close()

# Function to retrieve data
def retrieve_data():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    
    # Retrieving all students
    c.execute('SELECT * FROM student')
    all_students = c.fetchall()
    print("All Students:")
    for student in all_students:
        print(student)
    
    # Retrieving selected columns of students
    c.execute('SELECT id, email, batch_id FROM student')
    selected_students = c.fetchall()
    print("\nSelected Students:")
    for student in selected_students:
        print(student)
    
    # Retrieving student with name "Student 4"
    c.execute('SELECT * FROM student WHERE name=?', ("Student 4",))
    student_4 = c.fetchone()
    print("\nStudent 4:")
    print(student_4)
    
    # Retrieving students with "pak" in name
    c.execute('SELECT * FROM student WHERE name LIKE ?', ("%pak%",))
    pak_students = c.fetchall()
    print("\nStudents with 'pak' in name:")
    for student in pak_students:
        print(student)

    conn.close()


def main():
    create_tables()
    insert_data()
    retrieve_data()



if __name__ == "__main__":
    main()