## Coupling and Cohesion
Coupling and cohesion are essential concepts in software engineering that govern the relationships between different parts of your code. They significantly impact the maintainability, readability, and testability of your program.


### 1. Coupling
Coupling focuses on the interdependence between modules (functions, classes, etc.) in your program. Here's a breakdown of coupling levels:

- **High Coupling:** Modules are tightly knit and heavily rely on each other. Modifications in one module can easily cascade and affect others, making it challenging to modify or test individual parts.
- **Low Coupling:** Modules are independent with minimal interaction. Changes in one module have minimal impact on others, promoting modularity and easier maintenance.

#### Types of Coupling:
In Most to Least Coupling Ranking

**Data Coupling:** If the dependency between the modules is based on the fact that they communicate by passing only data, then the modules are said to be data coupled. In data coupling, the components are independent of each other and communicate through data. Module communications don’t contain tramp data. Example-customer billing system.

**Stamp Coupling:** In stamp coupling, the complete data structure is passed from one module to another module. Therefore, it involves tramp data. It may be necessary due to efficiency factors- this choice was made by the insightful designer, not a lazy programmer.

**Control Coupling:** If the modules communicate by passing control information, then they are said to be control coupled. It can be bad if parameters indicate completely different behavior and good if parameters allow factoring and reuse of functionality. Example- sort function that takes comparison function as an argument.

**External Coupling:** In external coupling, the modules depend on other modules, external to the software being developed or to a particular type of hardware. Ex- protocol, external file, device format, etc.

**Common Coupling:** The modules have shared data such as global data structures. The changes in global data mean tracing back to all modules which access that data to evaluate the effect of the change. So it has got disadvantages like difficulty in reusing modules, reduced ability to control data accesses, and reduced maintainability.

**Content Coupling:** In a content coupling, one module can modify the data of another module, or control flow is passed from one module to the other module. This is the worst form of coupling and should be avoided.



### 2. Cohesion
Cohesion dives into the internal structure of a single module. It describes how effectively the elements within a module work together towards a specific goal. Here's how cohesion can vary:

- **High Cohesion:** The elements within a module are tightly focused and perform a single, well-defined task. This makes the code easier to understand and reuse.
- **Low Cohesion:** The elements within a module are loosely related and handle multiple unrelated tasks. This makes the code harder to reason about and maintain.

### Types
In Most to Least Cohesion Ranking
1. **Functional Cohesion**: The module performs exactly one task or function.
   - **Example**: A class that handles user authentication by validating user credentials and generating authentication tokens.

2. **Sequential Cohesion**: The module performs tasks where the output of one part is the input to another part.
   - **Example**: A data processing pipeline where the data is cleaned, then transformed, and finally analyzed.

3. **Communicational Cohesion**: The module performs tasks that operate on the same data or produce data that is used together.
   - **Example**: A class that manages the customer database by adding, updating, and generating reports from customer records.

4. **Procedural Cohesion**: The module performs tasks that need to be executed in a specific order.
   - **Example**: A class that reads input data from a file, processes the data, and writes the output to another file.

5. **Temporal Cohesion**: The module performs tasks that are related by the timing at which they need to be executed.
   - **Example**: An initialization class that handles opening log files, initializing variables, and reading configuration files at start-up.

6. **Logical Cohesion**: The module performs tasks that are logically related by the type of logic used.
   - **Example**: A class that provides multiple sorting algorithms like bubble sort, quick sort, and merge sort.

7. **Coincidental Cohesion**: The module performs multiple, completely unrelated tasks.
   - **Example**: A utility class that contains methods for printing reports, calculating discounts, and managing user sessions.

### Benefits of Low Coupling and High Cohesion:

- **Maintainability:** Low coupling and high cohesion lead to code that's easier to maintain. Changes are simpler to localize and less likely to cause unintended side effects.
- **Readability:** Well-coupled and cohesive code is easier to understand for both you and other developers. Each module's purpose and interaction with others are clear.
- **Testability:** Low coupling allows you to test modules in isolation, simplifying the testing process and improving test coverage.

### Striking a Balance:

While aiming for low coupling and high cohesion is ideal, it's not always achievable in every scenario. Sometimes, a bit of coupling is necessary for functionality. The key is to find a balance that promotes modularity, maintainability, and testability without sacrificing functionality.


### Reference 
- https://www.geeksforgeeks.org/software-engineering-coupling-and-cohesion/