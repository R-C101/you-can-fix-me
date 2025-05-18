#include <cassert>
#include <iostream>
#include "cpp_003_fix_me.cpp"

int main() {
    std::cout << "* Running tests..." << std::endl;
    int* result1 = broken_addition(2, 3);
    assert(*result1 == 5);
    delete result1;

    int* result2 = broken_addition(-1, 1);
    assert(*result2 == 0);
    delete result2;

    int* result3 = broken_addition(0, 0);
    assert(*result3 == 0);
    delete result3;

    std::cout << "All tests passed!" << std::endl;
    return 0;
}
