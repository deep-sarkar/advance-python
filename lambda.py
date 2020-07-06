print("----- lambda -----")
"""
LAMBDA/ANANOMOUS Functions :
  Generally it is 1 line function used to perform small operations.
"""

a = lambda a:2*a   #example a : Takes 'a' as an argument and returns a*2
print('a :',a(6))

""""""

b = lambda b,c: b%c #example b : Takes 'b' and 'c' as an argument and returns b%c
print('b :',b(7,2))

""""""

def myfunc(n):        #example c : myfunc(n) takes a number as an argument and returns lambda function. 
  return lambda a : a * n # ie by this we can create one more 1 line function.

twice = myfunc(2)  #created a function twice which will return n*2 when a int argument is passed an argument
print('c :',twice(20)) #passed 20 in twice() will return 40

multiply = myfunc(3)
print('d :',multiply(3))



print("----- map() -----")
"""
map(func, *iterables) : it is used to perform some small operations to allthe elements in iterable ie. sequence like list.
 commonly we can use lambda function as a function argument.
"""
#example 1
marks = [40, 49, 31, 45, 43 , 41, 21, 33]

add_5_in_all_marks = list(map(lambda a:a+5,marks))
print('adding 5 to all the numbers in list using map :',add_5_in_all_marks)

#example 2
subjects = ['math', 'english','science']

subj_in_upper_case = list(map(str.upper, subjects))
print('subjects in upper case :',subj_in_upper_case)
