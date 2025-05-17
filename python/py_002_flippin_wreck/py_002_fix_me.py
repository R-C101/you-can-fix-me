"""
Problem ID: py_002
Name: Flip That Backwards

Instructions:
- Change the code inside the reverse_string function so that it works as intended
- The function should return the reversed UPPERCASE version of the string
- Do not modify any code outside of the function
- Run py_002_test_me.py to verify your solution works correctly
- Do not modify the py_002_test_me.py file as it's used to verify your solution
"""

def reverse_string(s):
    return s[::-1].upper 

print(reverse_string("Hello, World!"))