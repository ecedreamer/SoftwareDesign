# READ THIS MENDATORY 
Click this link: https://refactoring.guru/design-patterns
Another: https://www.oodesign.com/

## Design Patterns


Design patterns are reusable solutions to common problems encountered in software design. They provide a structured approach to solving design problems and promote code reuse, maintainability, and scalability. 

## Gang of Four (GoF) Design Patterns
- The Gang of Four (GoF) is a group of four authors who wrote the influential book "Design Patterns: Elements of Reusable Object-Oriented Software." 
- Four authors are Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides
- This book, published in 1994, cataloged 23 design patterns into three categories: Creational, Structural, and Behavioral. 
- These patterns were derived from their experience with designing software systems and captured common solutions to recurring design problems.

### Creational Patterns:
These patterns focus on object creation without specifying the exact class or subclass. They provide mechanisms for flexible and controlled object instantiation.

1. **Singleton Pattern**: Ensures that a class has only one instance and provides a global point of access to that instance.
    
    Eg. A logging class where only one instance needs to maintain the log entries.
    <img src="resources/singleton_class.png" width="500"/>

2. **Factory Pattern**: Defines an interface for creating an object, but allows subclasses to alter the type of objects that will be created.
  
    Eg. A document creation application where the Factory Method can create different document types (Word, PDF) based on user selection.
<img src="resources/factory_pattern_uml_diagram.jpg" width="800"/>

```python

from abc import ABC, abstractmethod

class Shape(ABC):
  """Abstract class representing a shape."""

  @abstractmethod
  def draw(self) -> None:
    pass

class Square(Shape):
  """Concrete class representing a square shape."""

  def draw(self) -> None:
    print("Drawing a square.")

class Circle(Shape):
  """Concrete class representing a circle shape."""

  def draw(self) -> None:
    print("Drawing a circle.")

class ShapeFactory:
  """Factory class for creating different shapes."""

  @staticmethod
  def create_shape(shape_type: str) -> Shape:
    """Creates a shape object based on the provided type."""
    if shape_type == "square":
      return Square()
    elif shape_type == "circle":
      return Circle()
    else:
      raise ValueError(f"Invalid shape type: {shape_type}")

# Usage example
def draw_shape(shape_type: str) -> None:
  """Function to draw a shape using the factory."""
  shape = ShapeFactory.create_shape(shape_type)
  shape.draw()

draw_shape("square")  # Output: Drawing a square.
draw_shape("circle")  # Output: Drawing a circle.
# draw_shape("invalid")  # Raises ValueError

```

3. **Abstract Factory Pattern**: Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
  
    Eg. A UI framework where the Abstract Factory can create different UI elements (buttons, text boxes) based on the desired platform (Windows, Mac).
    <img src="resources/abstract-factory-diagram.webp" width="800"/>

4. **Builder Pattern**: Separates the object construction process from its representation.
  
    Eg. Building a complex configuration object with multiple optional parameters.

      <img src="resources/builder_pattern.png" width="800"/>

5. **Prototype Pattern**: Creates new objects by cloning existing ones without dependency.
  
    Eg. Creating network connections where initial settings can be copied from a base prototype.
    <img src="resources/prototype-pattern.jpg" width="800"/>

### Structural Patterns:
These patterns focus on composing classes and objects to form larger structures and functionalities. They deal with how classes and objects are structured and how they collaborate.

1. **Adapter Pattern**: Allows objects with incompatible interfaces to work together by providing a wrapper that converts the interface of one class into another interface.

    Eg. Using a card reader adapter to make an old computer compatible with newer SD cards.
    <img src="resources/adapter-design-pattern.jpeg" width="800"/>


In the above diagram, 
- SQLDatabase is adaptee
- DatabaseInterface is Target
- DBAdapter is Adapter
  
```python
from abc import ABC, abstractmethod


class SQLDatabase:
    """ Target System for which we are making adapter """
    def execute_query(self, sql_query):
        print("Executing...")
        print(sql_query)
        print("Finished...")


class DatabaseInterface(ABC):  # ABC = AbstractBaseClass or Abstract Class is a class which can not be instantiated
    """ Interface for Desired System """
    @abstractmethod
    def fetch_data(self, table, condition):
        ...
        
    @abstractmethod
    def insert_data(self, table, **data):
        ...
        

class DBAdapter(DatabaseInterface):
    """ Adapter based on Desired Interface """
    def __init__(self, adaptee):
        self.adaptee = adaptee
    
    def fetch_data(self, table, condition):
        query = f"SELECT * FROM {table} WHERE {condition}"
        self.adaptee.execute_query(query)
        
    def insert_data(self, table, **data):
        student_name = data.get("name")
        student_address = data.get("address")
        query = f"INSERT INTO {table}qu(name, address) VALUES({student_name}, {student_address})"
        self.adaptee.execute_query(query)


def main():
    """ Adaptor Implementation Code """
    print("starting main")
    adaptee = SQLDatabase()
    adapter = DBAdapter(adaptee)
    print("Inserting Data")
    adapter.insert_data("Student", name="Dipak", address="Lalitpur")
    
    print("\nFetching Data")
    adapter.fetch_data("Student", condition="name=Dipak")
    
    
if __name__ == "__main__":
    main()

```

1. **Bridge Pattern**: The Bridge Pattern decouples an abstraction from its implementation so that the two can vary independently. This allows for more flexible and maintainable code.

    Eg.  Separate game rendering logic (abstraction) from graphics API (implementation) for platform-independent game development.

2. **Facade Pattern**: Provides a simplified interface to a complex system of classes, making it easier to use

    Eg. An ATM interface that hides the underlying complexities of account management and transaction processing.
    <img src="resources/facade_pattern.png" width="800"/>

3. **Composite Pattern**: Treats a group of objects as a single object and allows for recursive operations.

    Eg. A file system where folders and files can be treated similarly for operations like copying or deleting.

4. **Decorator Pattern**: Allows behavior to be added to individual objects dynamically, without affecting the behavior of other objects from the same class.

    Eg. Decorating a text editor with features like spell checking or grammar suggestions.
 
5. **Proxy Pattern**: A security proxy that checks user permissions before allowing access to a resource.

    Eg. A security proxy that checks user permissions before allowing access to a resource.

6. **Flyweight Pattern**: Makes efficient use of memory by sharing similar objects.

    Eg. Reusing character icons in a word processing application instead of creating a new object for each instance.

### Behavioral Patterns:
These patterns focus on communication and interaction between objects. They define ways for objects to communicate with each other and share information.

1. **Strategy Pattern**: Defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

    Eg. A sorting algorithm where the strategy can be chosen (bubble sort, quick sort) based on data size.
    <img src="resources/strategy_pattern.png" width="800"/>

2. **Observer Pattern**: Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

    Eg. A stock market application where observers (investor accounts) are notified of price changes in specific stocks.

3. **Iterator Pattern**: Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

    Eg. Looping through items in a shopping cart without needing to know the internal storage implementation.

4. **Command Pattern**: Encapsulates a request as an object, thereby allowing parameterization of clients with queues, requests, and operations.

    Eg. Macro buttons in a graphics application that store and execute a sequence of commands.
    <img src="resources/command-pattern.png" width="800"/>

5. **Template Method Pattern**: EDefines the skeleton of an algorithm in an operation, deferring some steps to subclasses.

    Eg. A data processing pipeline where the overall flow is defined but specific processing steps are implemented in subclasses.


6. **State Pattern**: The State design pattern allows an object to alter its behavior when its internal state changes, making it appear as if the object changes its class. 

    Eg. A light switch that changes its behavior (on/off) based on its internal state.
    <img src="resources/state-pattern.jpg" width="800"/>

```python

from abc import ABC, abstractmethod

# Context class
class LightSwitch:
    def __init__(self):
        self.off_state = OffState(self)
        self.on_state = OnState(self)
        self.state = self.off_state

    def set_state(self, state):
        self.state = state

    def toggle(self):
        self.state.toggle()

# State interface
class State(ABC):
    def __init__(self, light_switch):
        self.light_switch = light_switch

    @abstractmethod
    def toggle(self):
        pass

# Concrete states
class OffState(State):
    def toggle(self):
        print("Switching to ON")
        self.light_switch.set_state(self.light_switch.on_state)

class OnState(State):
    def toggle(self):
        print("Switching to OFF")
        self.light_switch.set_state(self.light_switch.off_state)

# Client code
def main():
    light_switch = LightSwitch()
    
    # Toggle the switch a few times
    light_switch.toggle()  # Switching to ON
    light_switch.toggle()  # Switching to OFF
    light_switch.toggle()  # Switching to ON
    light_switch.toggle()  # Switching to OFF

if __name__ == "__main__":
    main()

```

7. **Memento Pattern**: Captures and externalizes an object's internal state at a specific point in time. The saved state (memento) can be used to restore the object to its original state.

    Eg. Saving and restoring the state of a game to allow players to resume from previous checkpoints.

8. **Chain of Responsibility Pattern**: Allows a set of classes to handle a request one by one in a chain until the request is handled.

    Eg. A helpdesk system where a request is escalated to different support levels based on its complexity.

9. **Interpreter Pattern:**  Creates an interpreter for a specific language to execute a representation of that language.

    Eg. A calculator application that interprets mathematical expressions entered by the user.

10. **Mediator Pattern:** Defines an object that coordinates communication between a group of objects.

    Eg. An air traffic control system that coordinates communication between airplanes and ground control.

11. **Visitor Pattern:** Defines an operation to be performed on elements of an object structure without changing the structure itself.

    Eg. Analyzing a syntax tree in a compiler using a visitor pattern to perform different operations on different types of nodes.


## References: 
- You can see all design pattern class diagrams here 
    
    https://online.visual-paradigm.com/diagrams/templates/class-diagram/
- Read this mendatorily: 
    
    https://refactoring.guru/design-patterns

- Its also interesting series if you want to go deep
  
    https://www.youtube.com/watch?v=v9ejT8FO-7I&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&ab_channel=ChristopherOkhravi