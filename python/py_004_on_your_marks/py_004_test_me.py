"""
Do not modify this file!
This file contains tests to verify your solution works correctly.
Run this file to check if your solution passes all test cases.
"""

from py_004_fix_me import average_student_scores

def test_average_student_scores():
    assert average_student_scores({'Alice': [90, 80, 70]}) == {'Alice': 80.0}
    assert average_student_scores({'Bob': [50, 75], 'Eve': [100]}) == {'Bob': 62.5, 'Eve': 100.0}
    assert average_student_scores({}) == {}
    return True

if __name__ == "__main__":
    print(test_average_student_scores())