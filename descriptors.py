"""
-These are special type of protocols used to set, get or delete any instance from a class.
-This is simillar to getter and setter method used in other programming language like java in encapsulation
-There are 3 predefined descriptors in python. Three different methods that are __getters__(),
     __setters__(), and __delete__(). If any of these 3 defined for an object then called as descriptor.
"""
class Employee(object):

     def __init__(self, name=''):
          self.__name = name

     @property
     def name(self):
          return "Getting name :" + self.__name
     
     @name.setter
     def name(self, name):
          print('Setting name :', name)
          self.__name = name
     
     @name.deleter
     def name(self):
          print("Deleting name :",self.__name)
          del self.__name
     

emp1 = Employee("Deep")
print(emp1.name)
emp1.name = "Rajnikant"
print(emp1.name)
del emp1.name


