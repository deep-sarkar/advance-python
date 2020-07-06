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

def myfunc(n):        #example 
  return lambda a : a * n

twice = myfunc(2)
print('c :',twice(20))

multiply = myfunc(3)
print('d :',multiply(3))





