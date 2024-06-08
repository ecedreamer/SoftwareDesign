### ACID Properties of a Database

- **Atomicity**: Ensures that each transaction is treated as a single, indivisible unit of work. Either all operations within the transaction are successfully completed and committed to the database, or none of them are. If any part of the transaction fails, the entire transaction is rolled back to its original state.
  
- **Consistency**: Ensures that the database remains in a valid state before and after each transaction. Transactions must adhere to all constraints, rules, and validation criteria defined in the database schema. Any transaction that violates the integrity constraints of the database is aborted, ensuring that the database remains consistent.

- **Isolation**: Ensures that the execution of one transaction is isolated from the effects of other concurrent transactions. Each transaction operates as if it were the only transaction executing on the database, preventing interference between transactions. Isolation levels define the degree to which transactions are isolated from each other.

- **Durability**: Guarantees that once a transaction is committed, its changes are permanent and will not be lost, even in the event of a system failure or crash. This property ensures that the effects of committed transactions persist in the database, providing reliability and data integrity.