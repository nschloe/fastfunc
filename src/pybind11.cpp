#include <functional>
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;


template <typename T, typename OP>
void
at(
    py::array_t<T> array,
    py::array_t<int64_t> idx,
    py::array_t<T> vals
    )
{
  // <https://github.com/pybind/pybind11/issues/1412#issuecomment-391706305>
  auto r1 = array.template mutable_unchecked<2>();
  auto r2 = idx.unchecked<1>();
  auto r3 = vals.template unchecked<2>();

  if (r2.shape(0) != r3.shape(0))
    throw std::runtime_error("Input shapes must match");

  if (r1.shape(1) != r3.shape(1))
    throw std::runtime_error("Input shapes must match");

  for (ssize_t k=0; k < r2.shape(0); k++)
    for (ssize_t j=0; j < r1.shape(1); j++)
      r1(r2(k), j) = OP()(r1(r2(k), j), r3(k, j));

  return;
};

PYBIND11_MODULE(_fastfunc, m) {
  m.def("_add_at", &at<int64_t, std::plus<int64_t>>);
  m.def("_add_at", &at<double, std::plus<double>>);

  m.def("_subtract_at", &at<int64_t, std::minus<int64_t>>);
  m.def("_subtract_at", &at<double, std::minus<double>>);

  m.def("_multiply_at", &at<int64_t, std::multiplies<int64_t>>);
  m.def("_multiply_at", &at<double, std::multiplies<double>>);

  m.def("_divide_at", &at<int64_t, std::divides<int64_t>>);
  m.def("_divide_at", &at<double, std::divides<double>>);
}
