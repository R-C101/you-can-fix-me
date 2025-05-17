#include <iostream>
#include <cassert>
#include "cpp_001_fix_me.cpp"

int main() {
    assert(sum_two_numbers(2, 3) == 5);
    assert(sum_two_numbers(-1, 1) == 0);
    assert(sum_two_numbers(0, 0) == 0);
    std::cout << "All tests passed!" << std::endl;
    return 0;
}
