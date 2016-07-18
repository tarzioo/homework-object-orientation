"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   Encapsulation. Keeping everything 'together'

   Abstraction. It reduces complexity. It can hide details we don't need.

   Polymorphism. It allows flexibility of types without conditionals. Interchangeability
   of components

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

#super class called AbstractStudentInfo
class AbstractStudentInfo(object):
    pass

#sub class called Student. Its attributes are first_name, last_name and address
class Student(AbstractStudentInfo):

    #dunder init method
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address



#subclass called Question. It will take in question and correct_answer as
# #parameters and set as class attributes and bind them to a dictionary, questions.
# class Question(object):

#     def __init__(self):
#         self.current_dict = {}

#     def add_question(self, question, correct_answer):
#         self.question = question
#         self.correct_answer = correct_answer

#         self.current_dict[question] = correct_answer
#         print self.current_dict
  
#         return self.current_dict

# question1 = Question()
# # ('what color is the sky', 'blue')
# question2 = Question()
# # ('what color is the grass', 'green')
# question3 = Question()
# # ('what color is the sun', 'yellow')


class Question(AbstractStudentInfo):

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_question(self, question, correct_answer):
        print self.question    


#subclass called Exam, It takes in the questions dictionary from the Question class
#it also has class attributes of 'exam_name'
class Exam(AbstractStudentInfo):
    score = 0


    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        super(Exam, self).    

