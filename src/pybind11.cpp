#include "add_at.hpp"

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(_fastfunc, m) {
  m.def("add_at", &add_at_int);
  m.def("add_at", &add_at_double);
}
