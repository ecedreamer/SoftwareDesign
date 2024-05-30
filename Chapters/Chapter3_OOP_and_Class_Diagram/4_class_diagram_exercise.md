1. Create class diagram of an ecommerce applications on the basis of following problem statement:

In the ecommerce application, customers should be able to search product, place orders, make payment and get delivery. Products are classified in diffrent categories.

====> 
## Entities:

### Customer:

#### Attributes:
    CustomerID (Primary Key)
    Name
    Email
    ShippingAddress (Foreign Key to Address)
    BillingAddress (Foreign Key to Address)

### Product:

#### Attributes:
    ProductID (Primary Key)
    Name
    Description
    Price
    Stock
    CategoryID (Foreign Key to Category)

### Category:

#### Attributes:
    CategoryID (Primary Key)
    Name

### Order:

#### Attributes:
    OrderID (Primary Key)
    CustomerID (Foreign Key to Customer)
    OrderDate
    OrderStatus (e.g., "Pending", "Processing", "Shipped", "Delivered")

### Order_Item:

#### Attributes:
    OrderItemID (Primary Key)
    OrderID (Foreign Key to Order)
    ProductID (Foreign Key to Product)
    Quantity

### Payment:

#### Attributes:
    PaymentID (Primary Key)
    OrderID (Foreign Key to Order)
    PaymentMethod (e.g., "Credit Card", "Debit Card")
    PaymentStatus (e.g., "Authorized", "Declined", "Completed")

### Address:

#### Attributes:
    AddressID (Primary Key)
    Street
    City
    State
    Zipcode


## Relationships:
    - One Customer can have many Orders (1:N).
    - One Order belongs to one Customer (N:1).
    - One Order can have many Order_Items (1:N).
    - One Order_Item belongs to one Order (N:1).
    - One Order_Item refers to one Product (N:1).
    - One Product can be in one Category (N:1).
    - One Order is associated with one Payment (1:1).
    - One Customer can have multiple Addresses (1:N).
    - ShippingAddress and BillingAddress in Customer entity reference the Address entity (1:N).

2. Draw a UML class diagram to capture the following situation: “Every student is enrolled in a course. Each student may be enrolled in a set of units. Some units are core units for one or more courses and some units are elective units for one or more courses.”

Sample Assumption: a Course must have at least one Student enrolled in it and, as every student is enrolled in a Course, the relationship between Course and Student is 1-to-many. Assuming that elective units can be shared by different courses, between Course and ElectiveUnit is a many-to-many relationship (Similarly between Course and CoreUnit). 










