/*
Problem ID: cpp_001
Name: That Pointer Problem

Instructions:
- Fix the bug in the function below.
- Do not modify anything outside the buggy function.
- Run the test file to check your fix.
*/

#include <iostream>

int* broken_addition(int a, int b) {
    int sum = a + b;
    return &sum; // Uh-oh! Returning address of local variable
}


