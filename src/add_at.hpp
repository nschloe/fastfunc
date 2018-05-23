#ifndef ADD_AT_HPP
#define ADD_AT_HPP

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

#include <iostream>

namespace py = pybind11;

py::array_t<int>
add_at(
    py::array_t<int> array,
    py::array_t<int> idx,
    py::array_t<int> vals
    )
{
  auto buf0 = array.request();
  auto buf1 = idx.request();
  auto buf2 = vals.request();

  if (buf1.size != buf2.size)
    throw std::runtime_error("Input shapes must match");

  int *ptr0 = (int *) buf0.ptr;
  int *ptr1 = (int *) buf1.ptr;
  int *ptr2 = (int *) buf2.ptr;

  for (int k = 0; k < buf1.shape[0]; k++)
      ptr0[ptr1[k]] += ptr2[k];

  return array;
}

#endif // ADD_AT_HPP
