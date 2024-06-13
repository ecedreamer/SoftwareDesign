# Example Table NOT in 1NF

| OrderID | CustomerName | OrderDate   | Products            |
|---------|--------------|-------------|---------------------|
| 1       | Alice        | 2024-06-01  | [101, 102]          |
| 2       | Bob          | 2024-06-02  | [103]               |
| 3       | Charlie      | 2024-06-03  | [101, 103, 104]     |


## Example Table NOT in 2NF

| OrderID | ProductID | OrderDate   | ProductName   |
|---------|-----------|-------------|---------------|
| 1       | 101       | 2024-06-01  | Widget A      |
| 1       | 102       | 2024-06-01  | Widget B      |
| 2       | 103       | 2024-06-02  | Gadget X      |
| 2       | 104       | 2024-06-02  | Gadget Y      |
| 3       | 101       | 2024-06-03  | Widget A      |

## Example Table Not in 3NF

| OrderID | CustomerName | CustomerCity | ProductID | ProductName   | ProductCategory |
|---------|--------------|--------------|-----------|---------------|-----------------|
| 1       | Alice        | New York     | 101       | Widget A      | Electronics     |
| 1       | Alice        | New York     | 102       | Widget B      | Electronics     |
| 2       | Bob          | Los Angeles  | 103       | Gadget X      | Electronics     |
| 3       | Charlie      | Chicago      | 101       | Widget A      | Electronics     |
| 3       | Charlie      | Chicago      | 103       | Gadget X      | Electronics     |
| 3       | Charlie      | Chicago      | 104       | Gadget Y      | Electronics     |
