"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   Encapsulation.
   Instantiation
   Polymorphism

2. What is a class?
    It is a type of 'thing'. It is like a 'smarter dictionary'. They can define attributes
    and methods

3. What is an instance attribute?
    It is an individual attribute of an instance. For example, in the class Food,
    if we create an instance of the class Food and bind it to 'spagetti', we can
    define instance attributes for just the instance spagetti. These attributes
    such as 'italian', 'meatballs', can be defined to just that specific instance
    attribute of spagetti that ultimately stems from the parent class Food.

4. What is a method?
    It is similar to a function but it is defined in a clas. It ALWAYS has at least 
    one parameter, self and if there are more than one paramter, it will ALWAYS
    begin with self.


5. What is an instance in object orientation?
    It is an object of the class we are calling from. Each class can have as many
    instances, and they will all have similar attributes based on that classes
    attributes. Each instance can go futher and define its own instance attributes
    but it will have simalarities to the class it was instantiated from.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
    A class may list it's own generic attributes. For example, a Food class may
    set generic attributes of 'name, calories, food type'. Every instance
    of this class will have these same attributes that can either default to a generic
    value or have its own unique value that is set directly on the object.



"""


# Parts 2 through 5:
# Create your classes and class methods

#super class called Student
class Student(object):
    student_info = {}

    #dunder init method
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

print student_info

class Exam(Student):

    def __init__(self):
        self.questions = []