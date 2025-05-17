"""
Do not modify this file!
This file contains tests to verify your solution works correctly.
Run this file to check if your solution passes all test cases.
"""

from py_001_fix_me import sum_two_numbers

def test_sum():
    assert sum_two_numbers(2, 3) == 5
    assert sum_two_numbers(-1, 1) == 0
    assert sum_two_numbers(0, 0) == 0
    return True

if __name__ == "__main__":
    print(test_sum())