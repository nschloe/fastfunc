#ifndef ADD_AT_HPP
#define ADD_AT_HPP

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

#include <iostream>

namespace py = pybind11;

void
add_at_int(
    py::array_t<int64_t> array,
    py::array_t<int64_t> idx,
    py::array_t<int64_t> vals
    )
{
  auto r = array.mutable_unchecked<1>();
  auto buf1 = idx.request();
  auto buf2 = vals.request();

  if (buf1.size != buf2.size)
    throw std::runtime_error("Input shapes must match");

  int64_t *ptr1 = (int64_t *) buf1.ptr;
  int64_t *ptr2 = (int64_t *) buf2.ptr;

  for (ssize_t k=0; k < buf1.shape[0]; k++)
    r(ptr1[k]) += ptr2[k];

  return;
}

void
add_at_double(
    py::array_t<double> array,
    py::array_t<int64_t> idx,
    py::array_t<double> vals
    )
{
  auto r = array.mutable_unchecked<1>();
  auto buf1 = idx.request();
  auto buf2 = vals.request();

  if (buf1.size != buf2.size)
    throw std::runtime_error("Input shapes must match");

  int64_t *ptr1 = (int64_t *) buf1.ptr;
  double *ptr2 = (double *) buf2.ptr;

  for (ssize_t k=0; k < buf1.shape[0]; k++)
    r(ptr1[k]) += ptr2[k];

  return;
}
#endif // ADD_AT_HPP
