## Database Normalization
Database normalization is a process of organizing data in a relational database to minimize redundancy and improve data integrity. It involves structuring your database into multiple tables with defined relationships between them. This approach offers several advantages:

**Reduced Data Redundancy:** By eliminating duplicate data entries, you save storage space and minimize the chance of inconsistencies arising from updates in multiple places.

**Improved Data Integrity:** Normalization ensures data remains accurate and consistent throughout the database. Updates made in one table are reflected wherever the data is referenced.

**Enhanced Data Efficiency:** Normalized databases allow for faster retrieval and manipulation of specific data sets.


## Dependencies

### 1. Functional Dependency
Given a relation (table) R, an attribute A (or a set of attributes) is said to functionally determine another attribute B if, for every pair of tuples (rows) in R, whenever the values of A are the same, the values of B are also the same. This is denoted as A→B.

In other words, if two rows of a table have the same value for attribute A, then they must have the same value for attribute B.

**Example:** In a Customers table with attributes customer_id, customer_name, and city, the FD customer_id -> customer_name holds true. This means that knowing the customer_id uniquely determines the customer_name.

# Customers Table

| customer_id | customer_name | city       |
|-------------|---------------|------------|
| 1           | Alice         | New York   |
| 2           | Bob           | Los Angeles|
| 3           | Carol         | Chicago    |



### 2. Partial Dependency
A partial dependency (PD) is a special case of a functional dependency. It occurs when a determinant is only a part of the candidate key (all attributes that uniquely identify a row). In simpler terms, a non-key attribute depends on only a part of the key.

**Example:** Consider a OrderedProducts table
| OrderID | ProductID | OrderDate   | ProductName   | Price  |
|---------|-----------|-------------|---------------|--------|
| 1       | 101       | 2024-06-01  | Widget A      | 5000   |
| 1       | 102       | 2024-06-01  | Widget B      | 7000   |
| 2       | 103       | 2024-06-02  | Gadget X      | 3000   |
| 2       | 104       | 2024-06-02  | Gadget Y      | 2000   |
| 2       | 102       | 2024-06-02  | Gadget B      | 7000   |
| 3       | 101       | 2024-06-03  | Widget A      | 5000   |

- Primary key: (OrderID, ProductID)
Functional Dependencies: 
    - OrderID → OrderDate
    - ProductID → ProductName, Price
    - 
Partial Dependencies:

    - OrderID → OrderDate
    - ProductID → ProductName, Price


### 3. Transitive Dependency

A transitive dependency (TD) is an indirect dependency between attributes. It occurs when two FDs exist: X -> Y and Y -> Z. The transitive dependency then implies X -> Z, even though there's no direct FD between X and Z.

A transitive dependency occurs when one non-key attribute in a table depends on another non-key attribute, which itself depends on the table's primary key (or a part of it). This creates a chain of dependencies where an attribute indirectly depends on the primary key through another non-key attribute.

**Example:** 

| CourseID | CourseName       | LecturerName | Department       |
|----------|------------------|--------------|------------------|
| CS101    | Computer Science | Prof. Smith  | Computer Science |
| MATH101  | Mathematics      | Prof. Jones  | Mathematics      |
| PHYS101  | Physics          | Prof. Brown  | Physics          |
| CHEM101  | Chemistry        | Prof. Green  | Chemistry        |

Functional Dependency: CourseID → CourseName, LecturerName, Department

Transitive Dependency: Department → LecturerName

## Database Anomaly

### 1. Insert Anomaly
- An insertion anomaly occurs when certain attributes cannot be added to the database without the presence of other attributes.
- Example: Suppose we have a database where student information is stored, but we can only add a new student if the student enrolls in at least one course. If we try to add a student without any course enrollment, the insertion would fail, causing an anomaly.

### 2. Update Anomaly:
- An update anomaly occurs when updating data in a way that leads to inconsistency because changes are not correctly propagated to all relevant records.
- Example: In a database of customer orders, if a customer changes their address, and this information is stored redundantly in multiple order records, updating the address in one place but forgetting to update it in all related order records could lead to inconsistency.

### 3. Delete Anomaly
- A deletion anomaly occurs when deleting certain data causes unintended loss of other data that is still needed.
- Example: Consider a database of a company's employees and projects they are working on. If we delete information about an employee who is the only one working on a particular project, we might unintentionally lose information about that project as well.



# Example Table: Student_Course

| StudentID | StudentName | CourseID | CourseName   | Instructor    |
|-----------|-------------|----------|--------------|---------------|
| 1         | Alice       | 101      | Math         | Mr. Smith     |
| 2         | Bob         | 102      | Physics      | Ms. Johnson   |
| 3         | Carol       | 101      | Math         | Mr. Smith     |
| 4         | Dave        | 103      | History      | Mr. Brown     |

## 1. Insertion Anomaly

An insertion anomaly occurs when you cannot insert data into the database without having all necessary attributes available. In our example:

- **Issue:** You cannot insert a new course into the database unless at least one student is enrolled in it. This is because the table structure ties courses directly to students.
- **Example:** If you want to add a new course "Biology" (CourseID 104) and there are currently no students enrolled in it, you cannot insert it into the table without violating integrity constraints.

## 2. Deletion Anomaly

A deletion anomaly occurs when deleting data leads to unintended loss of other data that is still necessary. In our example:

- **Issue:** If you delete information about a student who is the only one enrolled in a particular course, you would lose information about that course altogether.
- **Example:** If you delete StudentID 2 (Bob) who is the only student enrolled in "Physics" (CourseID 102), the entire record for CourseID 102 (Physics) would be lost from the table, even though "Physics" as a course still exists.

## 3. Update Anomaly

An update anomaly occurs when updating data in a way that leads to inconsistencies because changes are not propagated correctly. In our example:

- **Issue:** If you update information about a course (like changing the Instructor), you would need to update it in multiple places if the same course is taught to multiple students.
- **Example:** If Mr. Smith (Instructor) decides to change his name to Dr. Smith, you would need to update every record where Mr. Smith is listed as the instructor. If you forget to update one of these records, inconsistencies can arise where the instructor's name is different for the same course.


## Normal Forms

### First Normal Form (1NF):
Ensures all data items within a column are atomic (single value) and there are no repeating groups within a table.

### Second Normal Form (2NF):
Complies with 1NF and eliminates partial dependencies. This occurs in a table where there is a primary key composed of more than one key. 
A partial dependency occurs when a non-key attribute depends on only a part of the primary key.

### Third Normal Form (3NF)
Adheres to 2NF and removes transitive dependencies. This occurs when one non-key attribute depends on another non-key attribute, which in turn depends on the primary key.


## Video References:
- Anamoly and Normalization
  - https://www.youtube.com/watch?v=xoTyrdT9SZI&list=PLLGlmW7jT-nTr1ory9o2MgsOmmx2w8FB3
- Database Anamoly
  - https://www.youtube.com/watch?v=yAkttVZbGaI&ab_channel=ZeenatHasanAcademy
  - https://www.youtube.com/watch?v=fFjuUTijtYQ&t=22s&ab_channel=StudyTable
- Normalization
  - https://www.youtube.com/watch?v=xPzgK6sOCfg&ab_channel=SaghirSchool
  - https://www.youtube.com/watch?v=9nm_Cj4M63Q&ab_channel=TechCoach