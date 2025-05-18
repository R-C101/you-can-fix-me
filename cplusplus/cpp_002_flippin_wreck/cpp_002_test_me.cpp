#include <cassert>
#include <iostream>
#include "cpp_002_fix_me.cpp"

int main() {
    assert(reverse_string("hello") == "olleh");
    assert(reverse_string("abc") == "cba");
    assert(reverse_string("") == "");
    std::cout << "All tests passed!" << std::endl;
    return 0;
}
