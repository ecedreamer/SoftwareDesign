1. Normalize the table below in 1nf

Order Table
| OrderID | CustomerName | OrderDate   | Products            |
|---------|--------------|-------------|---------------------|
| 1       | Alice        | 2024-06-01  | [101, 102]          |
| 2       | Bob          | 2024-06-02  | [103]               |
| 3       | Charlie      | 2024-06-03  | [101, 103, 104]     |


2. Normalize the table in 2nf.
OrderedProduct Table
| OrderID | ProductID | OrderDate   | ProductName   | Price  |
|---------|-----------|-------------|---------------|--------|
| 1       | 101       | 2024-06-01  | Widget A      | 5000   |
| 1       | 102       | 2024-06-01  | Widget B      | 7000   |
| 1       | 102       | 2024-06-01  | Widget B      | 7000   |
| 2       | 103       | 2024-06-02  | Gadget X      | 3000   |
| 2       | 104       | 2024-06-02  | Gadget Y      | 2000   |
| 2       | 102       | 2024-06-02  | Widget B      | 7000   |
| 3       | 101       | 2024-06-03  | Widget A      | 5000   |

3. Normalize the table below in 1nf, 2nf and 3nf if necessary.
OrderDetail Table
| Order Number | Customer Name | Customer Address | Item   | Quantity | Price | Total |
|--------------|---------------|------------------|--------|----------|-------|-------|
| 101          | John Smith    | 123 Main St.     | Apple  | 2        | 1.00  | 2.00  |
| 102          | John Smith    | 123 Main St.     | Orange | 3        | 0.75  | 2.25  |
| 103          | Jane Doe      | 456 Oak Ave.     | Banana | 1        | 0.50  | 0.50  |
