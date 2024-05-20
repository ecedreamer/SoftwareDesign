### Sequence Diagram ###
- A sequence diagram is a type of interaction diagram that visualizes the flow of messages, events, and interactions between objects or components within a system over time. 
- It depicts the sequence of actions or processes that occur in a particular scenario or use case. 
- Sequence diagrams are commonly used in software development to model the behavior of systems, especially during the design phase.

In a sequence diagram:

**Participants:** The entities involved in the interaction are represented as "participants" or "actors." These can be objects, components, or external systems.

**Lifelines:** Each participant is depicted by a vertical dashed line called a "lifeline," which extends downwards representing the time span during which the participant is active.

**Messages:** Messages exchanged between participants are shown as arrows or lines connecting lifelines. These messages indicate communication or interactions between participants.

**Activation Boxes:** Optional activation boxes can be used to indicate when a participant is actively processing a message. These boxes are drawn on top of the lifeline and represent the duration of the participant's processing time.

**Return Messages:** Return messages indicate responses or acknowledgments to the initial messages. They are shown with dashed lines or arrows returning back to the sender.


### Example 1
```sequence
Title: E-commerce Purchase Sequence

participant User
participant Browser
participant Web Server
participant Database
participant Payment Gateway

User->Browser: Opens e-commerce website
Browser->Web Server: Requests homepage
Web Server->Database: Retrieves homepage data
Database-->Web Server: Sends homepage data
Web Server-->Browser: Sends homepage data
Browser->User: Displays homepage

User->Browser: Searches for a product
Browser->Web Server: Sends search query
Web Server->Database: Searches for product
Database-->Web Server: Sends search results
Web Server-->Browser: Sends search results
Browser->User: Displays search results

User->Browser: Selects a product
Browser->Web Server: Requests product details
Web Server->Database: Retrieves product details
Database-->Web Server: Sends product details
Web Server-->Browser: Sends product details
Browser->User: Displays product details

User->Browser: Adds product to cart
Browser->Web Server: Sends request to add to cart
Web Server->Database: Updates cart with product
Database-->Web Server: Confirms addition to cart
Web Server-->Browser: Confirms addition to cart
Browser->User: Updates cart display

User->Browser: Proceeds to checkout
Browser->Web Server: Sends request to checkout
Web Server->Database: Retrieves cart information
Database-->Web Server: Sends cart information
Web Server->Payment Gateway: Initiates payment process
Payment Gateway-->Web Server: Provides payment form
Web Server-->Browser: Displays payment form
Browser->User: Fills in payment details

User->Browser: Submits payment
Browser->Web Server: Sends payment information
Web Server->Payment Gateway: Processes payment
Payment Gateway->Bank: Requests payment authorization
Bank-->Payment Gateway: Provides payment authorization
Payment Gateway-->Web Server: Sends payment confirmation
Web Server->Database: Updates order status
Database-->Web Server: Confirms order status update
Web Server-->Browser: Displays order confirmation
Browser->User: Displays order confirmation


```


### Example 2
```
Title: Library Management System Sequence Diagram

participant User
participant LibrarySystem
participant Database
participant Librarian

User->LibrarySystem: Requests to borrow a book
LibrarySystem->Database: Checks book availability
Database-->LibrarySystem: Returns book availability
LibrarySystem->User: Informs user about book availability

alt Book available
    User->LibrarySystem: Confirms book borrowing
    LibrarySystem->Database: Updates book status
    Database-->LibrarySystem: Confirms book status update
    LibrarySystem->User: Confirms book borrowing
else Book not available
    LibrarySystem->User: Informs user that book is not available
end

User->LibrarySystem: Requests to return a book
LibrarySystem->Database: Updates book status
Database-->LibrarySystem: Confirms book status update
LibrarySystem->User: Confirms book return

User->LibrarySystem: Requests to renew a book
LibrarySystem->Database: Checks book renewability
Database-->LibrarySystem: Returns book renewability
LibrarySystem->User: Informs user about book renewability

alt Book can be renewed
    User->LibrarySystem: Confirms book renewal
    LibrarySystem->Database: Updates book renewal
    Database-->LibrarySystem: Confirms book renewal update
    LibrarySystem->User: Confirms book renewal
else Book cannot be renewed
    LibrarySystem->User: Informs user that book cannot be renewed
end

User->LibrarySystem: Searches for a book
LibrarySystem->Database: Retrieves book information
Database-->LibrarySystem: Returns book information
LibrarySystem->User: Displays search results

User->LibrarySystem: Requests to reserve a book
LibrarySystem->Database: Checks book availability
Database-->LibrarySystem: Returns book availability
LibrarySystem->User: Informs user about book availability for reservation

alt Book available for reservation
    User->LibrarySystem: Confirms book reservation
    LibrarySystem->Database: Updates book reservation status
    Database-->LibrarySystem: Confirms book reservation update
    LibrarySystem->User: Confirms book reservation
else Book not available for reservation
    LibrarySystem->User: Informs user that book is not available for reservation
end

Librarian->LibrarySystem: Adds new book to the system
LibrarySystem->Database: Inserts new book information
Database-->LibrarySystem: Confirms book insertion

Librarian->LibrarySystem: Removes a book from the system
LibrarySystem->Database: Deletes book information
Database-->LibrarySystem: Confirms book deletion

```