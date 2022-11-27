'''
# We import the entire module
import modul_a

test = "Modul B."
print(test)
print(modul_a.test)
courses = ["PE", "History", "Math"]
index = modul_a.find_index(courses, "PE")
print(index)  # Prints 0
'''

'''
# We import the entire module and call it m_a
import modul_a as m_a

test = "Modul B."
print(test)
print(m_a.test)
courses = ["PE", "History", "Math"]
index = m_a.find_index(courses, "PE")
print(index)  # Prints 0
'''

'''
# We import only find_index function and test variable
from modul_a import find_index, test

print(test)
test = "Modul B."
print(test)
courses = ["PE", "History", "Math"]
index = find_index(courses, "PE")
print(index)  # Prints 0
'''

# We import all functions and variables
from modul_a import *

print(test)
test = "Modul B."
print(test)
courses = ["PE", "History", "Math"]
index = find_index(courses, "PE")
print(index)  # Prints 0

# imports
# standard library modules
# external library modules
# modules inside the project (our code)
# import modul_a
# import modul_c
# import modul_d

print_sys_path()

import random
print(random.__file__)