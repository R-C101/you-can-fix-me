"""
Do not modify this file!
This file contains tests to verify your solution works correctly.
Run this file to check if your solution passes all test cases.
"""

from py_006_fix_me import worked_hours

def test_worked_hours():
    logs = ["2023-01-01T09:00:00", "2023-01-01T17:00:00"]
    assert abs(worked_hours(logs) - 8.0) < 0.01

    logs = ["2023-01-01T23:00:00", "2023-01-02T07:00:00"]
    assert abs(worked_hours(logs) - 8.0) < 0.01

    logs = [
        "2023-01-01T08:00:00", "2023-01-01T12:00:00",
        "2023-01-01T13:00:00", "2023-01-01T17:00:00"
    ]
    assert abs(worked_hours(logs) - 8.0) < 0.01
    return True

if __name__ == "__main__":
    print(test_worked_hours())
