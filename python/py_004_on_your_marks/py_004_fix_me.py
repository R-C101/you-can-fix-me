"""
Problem ID: py_004
Name: On Your Marks

Instructions:
- Change the code inside the average_student_scores function so that it works as intended
- The function should correctly compute averages for each student's score list
- Do not modify any code outside of the function
- Run py_004_test_me.py to verify your solution works correctly
- Do not modify the test_me.py file as it's used to verify your solution
"""

def average_student_scores(student_scores):
    """
    Given a dictionary of students and their list of scores,
    return a dictionary of students and their average score.
    """
    result = {}
    for student in student_scores:
        total = 0
        for score in student_scores[student]:
            total += student_scores
        result[student] = total
    return result
