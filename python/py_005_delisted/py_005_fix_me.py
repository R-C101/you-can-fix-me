"""
Problem ID: py_005
Name: Delisted

Instructions:
- Change the code inside the flatten_and_sort function so that it works as intended
- The function should flatten a list of lists and sort the result
- Do not modify any code outside of the function
- Run py_005_test_me.py to verify your solution works correctly
- Do not modify the test_me.py file as it's used to verify your solution
"""

def flatten_and_sort(data):
    """
    Takes a list of lists and returns a single flattened, sorted list.
    """
    flattened = []
    for item in data:
        flattened.append(item)
    return flattened.sort()
