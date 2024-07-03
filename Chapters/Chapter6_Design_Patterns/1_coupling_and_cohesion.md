## Coupling and Cohesion
Coupling and cohesion are essential concepts in software engineering that govern the relationships between different parts of your code. They significantly impact the maintainability, readability, and testability of your program.


### 1. Coupling
Coupling refers to the degree of direct interdependence between software modules. It measures how closely connected different modules or classes are within a system.

***High Coupling:***

- Modules are highly dependent on each other.
- Changes in one module are likely to affect other modules.
- It makes the system more difficult to maintain and understand.
- Reduces the potential for reusability.

***Low Coupling:***

- Modules have minimal dependencies on each other.
- Changes in one module have little impact on other modules.
- It makes the system easier to maintain and understand.
- Enhances the potential for reusability.

#### Types of Coupling:
In Least to Most Coupling Ranking

**Data Coupling:**  Data coupling occurs when classes share data through parameters. This is the lowest degree of coupling and is generally preferred.
```python
class Calculator:
    def add(self, a, b):
        return a + b

class Printer:
    def print_sum(self, a, b):
        calc = Calculator()
        result = calc.add(a, b)
        print(f"Sum: {result}")

printer = Printer()
printer.print_sum(5, 3)  # Output: Sum: 8

```

**Stamp Coupling:**  Stamp coupling occurs when classes share a composite data structure and only use a part of it.
```python
class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class AddressPrinter:
    def print_city(self, address):
        print(address.city)

address = Address("123 Main St", "Springfield", "IL")
person = Person("John Doe", address)
printer = AddressPrinter()
printer.print_city(person.address)
```

**Control Coupling:** Control coupling occurs when one class controls the flow of another by passing it information on what to do (e.g., a control flag).
```python
class Task:
    def execute(self, flag):
        if flag == 'start':
            print("Starting task")
        elif flag == 'stop':
            print("Stopping task")

class Controller:
    def __init__(self, task):
        self.task = task

    def run(self):
        self.task.execute('start')
        self.task.execute('stop')

task = Task()
controller = Controller(task)
controller.run()

```

**External Coupling:** External coupling occurs when classes share an externally imposed data format, communication protocol, or device interface.

```python
import json

class DataProcessor:
    def process(self, data):
        # Expects data in JSON format
        parsed_data = json.loads(data)
        print(parsed_data)

data = '{"name": "John", "age": 30}'
processor = DataProcessor()
processor.process(data)
```

**Common Coupling:** Common coupling occurs when multiple classes share global data.

```python
# Global variable
shared_data = {'count': 0}

class A:
    def increment(self):
        global shared_data
        shared_data['count'] += 1

class B:
    def decrement(self):
        global shared_data
        shared_data['count'] -= 1

a = A()
b = B()
a.increment()
b.decrement()
print(shared_data['count'])  # Output: 0

```

**Content Coupling:** Content coupling occurs when one class modifies or relies on the internal details of another class. This is the highest degree of coupling and is generally undesirable.

```python
class A:
    def __init__(self):
        self.value = 10

class B:
    def manipulate_a(self, a):
        # Directly accessing and modifying the internal state of class A
        a.value = 20

a = A()
b = B()
b.manipulate_a(a)
print(a.value)  # Output: 20

```



### 2. Cohesion
Cohesion refers to the degree to which the elements inside a module belong together. In software engineering, high cohesion within modules is desirable because it often results in more understandable, maintainable, and reusable code. Here's how cohesion can vary:

***Low Cohesion:***

- A module performs multiple, unrelated tasks.
- It makes the module harder to understand, maintain, and reuse.
- It indicates poor module design.

***High Cohesion:***

- A module performs a single, well-defined task.
- It makes the module easier to understand, maintain, and reuse.
- It indicates good module design.

### Types
In Most to Least Cohesion Ranking
1. **Functional Cohesion**: Functional cohesion occurs when elements are grouped because they all contribute to a single, well-defined task. This is the strongest form of cohesion.
   ```python
   class Calculator:
      def add(self, a, b):
         return a + b

      def subtract(self, a, b):
         return a - b

      def multiply(self, a, b):
         return a * b

      def divide(self, a, b):
         if b != 0:
               return a / b
         else:
               raise ValueError("Cannot divide by zero")

   calculator = Calculator()
   print(calculator.add(10, 5))
   print(calculator.subtract(10, 5))
   print(calculator.multiply(10, 5))
   print(calculator.divide(10, 5))
   ```

2. **Sequential Cohesion**:  Sequential cohesion occurs when elements are grouped because the output from one part is the input to another part.
   ```python
   class DataTransformer:
      def read_data(self):
         data = "raw data"
         print(f"Reading data: {data}")
         return data

      def transform_data(self, data):
         transformed_data = data.upper()
         print(f"Transforming data: {transformed_data}")
         return transformed_data

      def write_data(self, data):
         print(f"Writing data: {data}")

   transformer = DataTransformer()
   data = transformer.read_data()
   transformed_data = transformer.transform_data(data)
   transformer.write_data(transformed_data)
   ```

3. **Communicational Cohesion**: Communicational cohesion occurs when elements are grouped because they operate on the same data or contribute to the same task.
   ```python
   class StudentRecord:
      def __init__(self, name, grades):
         self.name = name
         self.grades = grades

      def calculate_average(self):
         return sum(self.grades) / len(self.grades)

      def print_record(self):
         print(f"Student: {self.name}")
         print(f"Grades: {self.grades}")
         print(f"Average: {self.calculate_average()}")

   record = StudentRecord("Alice", [85, 90, 78])
   record.print_record()
   ```

4. **Procedural Cohesion**: Procedural cohesion occurs when elements are grouped because they follow a specific sequence of execution.
   ```python
   class FileProcessor:
      def open_file(self, filename):
         print(f"Opening file: {filename}")

      def read_file(self, file):
         print("Reading file contents")

      def close_file(self, file):
         print("Closing file")

   processor = FileProcessor()
   processor.open_file("example.txt")
   processor.read_file("example.txt")
   processor.close_file("example.txt")
   ```

5. **Temporal Cohesion**: Temporal cohesion occurs when elements are grouped because they are related by the time they are executed.
   ```python
   class Initialization:
      def load_config(self):
         print("Loading configuration")

      def initialize_logging(self):
         print("Initializing logging")

      def initialize_database(self):
         print("Initializing database")

   init = Initialization()
   init.load_config()
   init.initialize_logging()
   init.initialize_database()
   ```

6. **Logical Cohesion**:  Logical cohesion occurs when elements are grouped because they are logically categorized to do the same thing, even if they are different by nature.
   ```python
   class InputHandler:
      def handle_keyboard_input(self, key):
         print(f"Handling keyboard input: {key}")

      def handle_mouse_input(self, event):
         print(f"Handling mouse input: {event}")

      def handle_touch_input(self, touch):
         print(f"Handling touch input: {touch}")

   input_handler = InputHandler()
   input_handler.handle_keyboard_input("A")
   input_handler.handle_mouse_input("click")
   input_handler.handle_touch_input("swipe")
   ```

7. **Coincidental Cohesion**: Coincidental cohesion occurs when parts of a module are grouped arbitrarily without any meaningful relationship. This is the weakest form of cohesion and is usually a sign of poor design.
   ```python
   class Utilities:
      def print_hello(self):
         print("Hello")

      def calculate_area(self, length, width):
         return length * width

      def convert_to_uppercase(self, text):
         return text.upper()

   utils = Utilities()
   utils.print_hello()
   print(utils.calculate_area(5, 3))
   print(utils.convert_to_uppercase("hello"))
   ```

### Benefits of Low Coupling and High Cohesion:

- **Maintainability:** Low coupling and high cohesion lead to code that's easier to maintain. Changes are simpler to localize and less likely to cause unintended side effects.
- **Readability:** Well-coupled and cohesive code is easier to understand for both you and other developers. Each module's purpose and interaction with others are clear.
- **Testability:** Low coupling allows you to test modules in isolation, simplifying the testing process and improving test coverage.

### Striking a Balance:

While aiming for low coupling and high cohesion is ideal, it's not always achievable in every scenario. Sometimes, a bit of coupling is necessary for functionality. The key is to find a balance that promotes modularity, maintainability, and testability without sacrificing functionality.


### Reference 
- https://www.geeksforgeeks.org/software-engineering-coupling-and-cohesion/