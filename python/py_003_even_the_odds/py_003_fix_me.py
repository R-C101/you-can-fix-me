"""
Problem ID: py_003
Name: Even the Odds

Instructions:
- Change the code inside the get_even_numbers function so that it works as intended
- The function should return only the even numbers from a list
- Do not modify any code outside of the function
- Run py_003_test_me.py to verify your solution works correctly
- Do not modify the test_me.py file as it's used to verify your solution
"""

def get_even_numbers(lst):
    return [x for x in lst if x % 2]  

print(get_even_numbers([1, 2, 3, 4, 5, 6]))




