"""
Problem ID: py_006
Name: Clocked In

Instructions:
- Change the code inside the worked_hours function so that it works as intended
- The function should calculate the total hours worked using clock-in/clock-out log timestamps
- Do not modify any code outside of the function
- Run py_006_test_me.py to verify your solution works correctly
- Do not modify the test_me.py file as it's used to verify your solution
"""

from datetime import datetime

def worked_hours(logs):
    """
    Given a list of employee clock-in and clock-out log entries (in ISO 8601),
    return the total hours worked in float.
    Logs are alternating: [in1, out1, in2, out2, ...]
    """
    total_seconds = 0
    for i in range(len(logs)):
        start = datetime.fromisoformat(logs[i])
        end = datetime.fromisoformat(logs[i+1])
        total_seconds += (end - start).seconds
    return total_seconds / 3600
