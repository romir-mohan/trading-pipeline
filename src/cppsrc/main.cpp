#include <iostream>
#include <pybind11/pybind11.h>

#include <pybind11/stl.h>


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

PYBIND11_MODULE(intern, m)
{
    pybind11::class_<intproj::DataClient>(m, "DataClient")
      .def(pybind11::init<>())
      .def("tick", &intproj::DataClient::tick);
}