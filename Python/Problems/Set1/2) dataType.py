# Datatype in python

"""
 1. Numberic Type
    int : Intergers
    float : For decimal numbers
    complex: Complex numbers in the form of `a+bj`
  
  2. Text Type

     str: Sequence of characters

  3. Sequence Types:
     
     list: Ordered collection of items that can have different data types. list are mutable

     tuple: Similar to list but immutable

     range: Represents arithmetic progression of integers. often used in loops

  4. Mapping Type: 
     
     dict: Dictonaries are unordered collections of key-value pairs. Each key must be unique
  
  5. Set Type: 
     
     set: unordered collections of unique elements. Set do not allow duplicate items.

  6. Boolean: 

     bool: Represetnts truth values 'True' or 'False'
"""

# numbers types

int_interger = 23
print('Type of int_integer is ', type(
    int_interger), 'and value is ', int_interger)
float_floatNumber = 23.4

print('Type of float_floatNumber is ', type(
    float_floatNumber), 'and value is ', float_floatNumber)

# Text Type
str_name = "this is string"
print('Type of str_name is ', type(
    str_name), 'and value is ', str_name)
# Boolean Type
bool_isTrue = True

# Sequence Type
list_python = ['orange', 'banana', 'papaya']
print('Type of list_python is ', type(
    list_python), 'and value is ', list_python)
tuple_python = (10, 20, 30)
print('Type of tuple_python is ', type(
    tuple_python), 'and value is ', tuple_python)
range_python = range(1, 5)

print('Type of range_pyhton is ', type(
    range_python), 'and value is ', range_python)
# Mapping Type
dict_python = {"name": 'jhon', "age": 30, "city": "new york"}
print('Type of dict_pyhton is ', type(
    dict_python), 'and value is ', dict_python)
set_python = {'orange', 'banana', 'papaya', 'orange'}
print('Type of str_name is ', type(
    set_python), 'and value is ', set_python)
