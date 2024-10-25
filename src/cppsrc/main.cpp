#include <iostream>
#include <pybind11/pybind11.h>

int main()
{
    std::cout << "hello\n";
}

int add(int a, int b)
{
    return a + b;
}

PYBIND11_MODULE(intern, m)
{
    m.def("add", &add, "Adds two numbers");
}
