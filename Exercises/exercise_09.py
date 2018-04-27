"""
Exercise 9


1) Write a decorator function that prints the:
     - real world time taken to run the function,
     - process time used to run the function, and
     - size of the return value (using sys.getsizeof())

2) Apply this decorator to the following functions:
    for_loop() - Create an empty list and append the values 1 to 1,000,000 to the list using a for loop
    list_comp() - Use list comprehension to create a list of all values 1 to 1,000,000
    numpy_list() - Create a numpy array with all values 1 to 1,000,000
    pandas_list() - Create a pandas data frame with all values 1 to 1,000,000
    generator_list() - Use generator comprehension to create a generator of the values 1 to 1,000,000
                (generator comprehension is the same as list comprehension, but uses () instead of [])

3) For each function in #2, write a new function that produces the log10 of every number from 1 to 1,000,000.
    for_loop_log()
    list_com_log()
    numpy_list_log()
    pandas_list_log()
    generator_list_log()

There are many different ways to complete this assignment and there is not one single best way that I would prefer.
The purpose of this exercise is to practice implementing a decorator function and gain experience and knowlege of
several different modules. As long as your submission does not circumvent the purpose of this exercise and completes
tasks 1, 2 and 3, then you will receive full credit.
"""

import sys
import numpy
import pandas
import time
import math
total = 1000000
#1
def time_decorator(my_def):
    def internal_wrapper():
        t0 = time.time()
        ta = time.process_time()
        def_result = my_def()
        t1 = time.time()
        tb = time.process_time()
        print("'{}' finished in {} seconds".format(my_def.__name__, t1-t0))
        print("'{}' finished in {} seconds".format(my_def.__name__, tb - ta))
        print("Result size is {}.".format(sys.getsizeof(def_result)))
        return def_result
    return internal_wrapper() # remember, 'internal_wrapper' is not the same as 'internal_wrapper()'

def squares():
    return [x**2 for x in range(1000000)]

def for_loop():
    ret_list = []
    for i in range(total):
        ret_list.append(i+1)
    return  ret_list

def list_comp():
    return [i+1 for i in range(total)]

def numpy_list():
    return numpy.array(list_comp())

def pandas_list():# - Create a pandas data frame with all values 1 to 1,000,000
    ret_list = pandas.DataFrame(list_comp())
    return ret_list

def generator_list():# - Use generator comprehension to create a generator of the values 1 to 1,000,000
    ret_list = (x+1 for x in range(total))
    return ret_list

k = time_decorator(for_loop)
k = time_decorator(list_comp)
k = time_decorator(numpy_list)
k = time_decorator(pandas_list)
k = time_decorator(generator_list)

def for_loop_log():
    ret_list = []
    for i in range(total):
        ret_list.append(math.log10(i+1))
    return ret_list

def list_comp_log():
    return [math.log10(i+1) for i in range(total)]

def numpy_list_log():
    return numpy.array(list_comp_log())

def pandas_list_log():# - Create a pandas data frame with all values 1 to 1,000,000
    return pandas.DataFrame(list_comp_log())

def generator_list_log():# - Use generator comprehension to create a generator of the values 1 to 1,000,000
    return (math.log10(x+1) for x in range(total))

k = time_decorator(for_loop_log)
k = time_decorator(list_comp_log)
k = time_decorator(numpy_list_log)
k = time_decorator(pandas_list_log)
k = time_decorator(generator_list_log)

quitter = 0