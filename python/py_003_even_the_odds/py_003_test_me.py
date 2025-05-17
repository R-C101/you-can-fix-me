"""
Do not modify this file!
This file contains tests to verify your solution works correctly.
Run this file to check if your solution passes all test cases.
"""

from py_003_fix_me import get_even_numbers

def test_get_even_numbers():
    assert get_even_numbers([1, 2, 3, 4, 5]) == [2, 4]
    assert get_even_numbers([0, -2, -3]) == [0, -2]
    assert get_even_numbers([1, 3, 5]) == []
    return True

if __name__ == "__main__":
    print(test_get_even_numbers())
