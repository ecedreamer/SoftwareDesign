
## ER Diagram
An Entity Relationship Diagram is a diagram that represents relationships among entities in a database.

### Entity
The building blocks of an ERD are entities, which represent real-world objects, concepts, or events that you want to store information about in your database. Examples of entities in a library management system could be Books, Authors, and Members.

### Attributes
While not directly shown in the ERD itself, entities are composed of attributes, which are essentially the specific characteristics or properties that define an entity.  For example, attributes of a Book entity might include title, author_id (foreign key referencing the Authors table), genre, and publication_date.

### Relationship & Cardinality
ERD also depicts the relationships between these entities with cardinality
It defines the numerical attributes of the relationship between two entities or entity sets. The three main cardinal relationships are one-to-one, one-to-many, and many-many. 
  1. A one-to-one example would be one student associated with one mailing address. 
  2. A one-to-many example (or many-to-one, depending on the relationship direction): One student registers for multiple courses, but all those courses have a single line back to that one student.
  3. A many-to-one example (or many-to-one, depending on the relationship direction): One student registers for multiple courses, but all those courses have a single line back to that one student. 
  4. Many-to-many example: Students as a group are associated with multiple faculty members, and faculty members in turn are associated with multiple students.

<img src="../../Images/entity_relationship.png" width="600">


### References: 
1. Video Tutorial: https://www.youtube.com/watch?v=HdaoufJNY_c&ab_channel=Drewity
2. https://www.lucidchart.com/pages/er-diagrams
3. https://www.visual-paradigm.com/guide/data-modeling/what-is-entity-relationship-diagram/