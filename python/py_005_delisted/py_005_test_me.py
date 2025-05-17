"""
Do not modify this file!
This file contains tests to verify your solution works correctly.
Run this file to check if your solution passes all test cases.
"""

from py_005_fix_me import flatten_and_sort

def test_flatten_and_sort():
    assert flatten_and_sort([[3, 1], [2]]) == [1, 2, 3]
    assert flatten_and_sort([]) == []
    assert flatten_and_sort([[5], [3, 4], [], [1]]) == [1, 3, 4, 5]
    return True

if __name__ == "__main__":
    print(test_flatten_and_sort())
