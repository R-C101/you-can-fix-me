"""
Do not modify this file!
This file contains tests to verify your solution works correctly.
Run this file to check if your solution passes all test cases.
"""

from py_002_fix_me import reverse_string

def test_reverse_string():
    assert reverse_string("abc") == "CBA"
    assert reverse_string("Hello") == "OLLEH"
    assert reverse_string("") == ""
    return True

if __name__ == "__main__":
    print(test_reverse_string())
