#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

#include <iostream>

namespace py = pybind11;

namespace py = pybind11;

void
add_at_int(
    py::array_t<int64_t> array,
    py::array_t<int64_t> idx,
    py::array_t<int64_t> vals
    )
{
  auto r1 = array.mutable_unchecked<2>();
  auto r2 = idx.unchecked<1>();
  auto r3 = vals.unchecked<2>();

  if (r2.shape(0) != r3.shape(0))
    throw std::runtime_error("Input shapes must match");

  if (r1.shape(1) != r3.shape(1))
    throw std::runtime_error("Input shapes must match");

  for (ssize_t k=0; k < r2.shape(0); k++)
    for (ssize_t j=0; j < r1.shape(1); j++)
      r1(r2(k), j) += r3(k, j);

  return;
};

void
add_at_double(
    py::array_t<double> array,
    py::array_t<int64_t> idx,
    py::array_t<double> vals
    )
{
  auto r1 = array.mutable_unchecked<2>();
  auto r2 = idx.unchecked<1>();
  auto r3 = vals.unchecked<2>();

  if (r2.shape(0) != r3.shape(0))
    throw std::runtime_error("Input shapes must match");

  if (r1.shape(1) != r3.shape(1))
    throw std::runtime_error("Input shapes must match");

  for (ssize_t k=0; k < r2.shape(0); k++)
    for (ssize_t j=0; j < r1.shape(1); j++)
      r1(r2(k), j) += r3(k, j);

  return;
};

void
subtract_at_int(
    py::array_t<int64_t> array,
    py::array_t<int64_t> idx,
    py::array_t<int64_t> vals
    )
{
  auto r1 = array.mutable_unchecked<2>();
  auto r2 = idx.unchecked<1>();
  auto r3 = vals.unchecked<2>();

  if (r2.shape(0) != r3.shape(0))
    throw std::runtime_error("Input shapes must match");

  if (r1.shape(1) != r3.shape(1))
    throw std::runtime_error("Input shapes must match");

  for (ssize_t k=0; k < r2.shape(0); k++)
    for (ssize_t j=0; j < r1.shape(1); j++)
      r1(r2(k), j) -= r3(k, j);

  return;
};

void
subtract_at_double(
    py::array_t<double> array,
    py::array_t<int64_t> idx,
    py::array_t<double> vals
    )
{
  auto r1 = array.mutable_unchecked<2>();
  auto r2 = idx.unchecked<1>();
  auto r3 = vals.unchecked<2>();

  if (r2.shape(0) != r3.shape(0))
    throw std::runtime_error("Input shapes must match");

  if (r1.shape(1) != r3.shape(1))
    throw std::runtime_error("Input shapes must match");

  for (ssize_t k=0; k < r2.shape(0); k++)
    for (ssize_t j=0; j < r1.shape(1); j++)
      r1(r2(k), j) -= r3(k, j);

  return;
};

void
multiply_at_int(
    py::array_t<int64_t> array,
    py::array_t<int64_t> idx,
    py::array_t<int64_t> vals
    )
{
  auto r1 = array.mutable_unchecked<2>();
  auto r2 = idx.unchecked<1>();
  auto r3 = vals.unchecked<2>();

  if (r2.shape(0) != r3.shape(0))
    throw std::runtime_error("Input shapes must match");

  if (r1.shape(1) != r3.shape(1))
    throw std::runtime_error("Input shapes must match");

  for (ssize_t k=0; k < r2.shape(0); k++)
    for (ssize_t j=0; j < r1.shape(1); j++)
      r1(r2(k), j) *= r3(k, j);

  return;
};

void
multiply_at_double(
    py::array_t<double> array,
    py::array_t<int64_t> idx,
    py::array_t<double> vals
    )
{
  auto r1 = array.mutable_unchecked<2>();
  auto r2 = idx.unchecked<1>();
  auto r3 = vals.unchecked<2>();

  if (r2.shape(0) != r3.shape(0))
    throw std::runtime_error("Input shapes must match");

  if (r1.shape(1) != r3.shape(1))
    throw std::runtime_error("Input shapes must match");

  for (ssize_t k=0; k < r2.shape(0); k++)
    for (ssize_t j=0; j < r1.shape(1); j++)
      r1(r2(k), j) *= r3(k, j);

  return;
};

void
divide_at_int(
    py::array_t<int64_t> array,
    py::array_t<int64_t> idx,
    py::array_t<int64_t> vals
    )
{
  auto r1 = array.mutable_unchecked<2>();
  auto r2 = idx.unchecked<1>();
  auto r3 = vals.unchecked<2>();

  if (r2.shape(0) != r3.shape(0))
    throw std::runtime_error("Input shapes must match");

  if (r1.shape(1) != r3.shape(1))
    throw std::runtime_error("Input shapes must match");

  for (ssize_t k=0; k < r2.shape(0); k++)
    for (ssize_t j=0; j < r1.shape(1); j++)
      r1(r2(k), j) /= r3(k, j);

  return;
};

void
divide_at_double(
    py::array_t<double> array,
    py::array_t<int64_t> idx,
    py::array_t<double> vals
    )
{
  auto r1 = array.mutable_unchecked<2>();
  auto r2 = idx.unchecked<1>();
  auto r3 = vals.unchecked<2>();

  if (r2.shape(0) != r3.shape(0))
    throw std::runtime_error("Input shapes must match");

  if (r1.shape(1) != r3.shape(1))
    throw std::runtime_error("Input shapes must match");

  for (ssize_t k=0; k < r2.shape(0); k++)
    for (ssize_t j=0; j < r1.shape(1); j++)
      r1(r2(k), j) /= r3(k, j);

  return;
};

PYBIND11_MODULE(_fastfunc, m) {
  m.def("_add_at", &add_at_int);
  m.def("_add_at", &add_at_double);

  m.def("_subtract_at", &subtract_at_int);
  m.def("_subtract_at", &subtract_at_double);

  m.def("_multiply_at", &multiply_at_int);
  m.def("_multiply_at", &multiply_at_double);

  m.def("_divide_at", &divide_at_int);
  m.def("_divide_at", &divide_at_double);
}
