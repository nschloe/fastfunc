# fastfunc

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/fastfunc/master.svg?style=flat-square)](https://circleci.com/gh/nschloe/fastfunc/tree/master)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/fastfunc.svg?style=flat-square)](https://codecov.io/gh/nschloe/fastfunc)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![speedy](https://img.shields.io/badge/speedy-gonzales-ff69b4.svg?style=flat-square)](https://github.com/nschloe/fastfunc)
[![PyPi Version](https://img.shields.io/pypi/v/fastfunc.svg?style=flat-square)](https://pypi.org/project/fastfunc)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/fastfunc.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/fastfunc)
[![PyPi downloads](https://img.shields.io/pypi/dm/fastfunc.svg?style=flat-square)](https://pypistats.org/packages/fastfunc)

[NumPy's own ufunc
operations](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ufunc.at.html)
are handy, but can be quite slow (see https://github.com/numpy/numpy/issues/5922 and
https://github.com/numpy/numpy/issues/11156).  Use `fastfunc` as a drop-in replacement
```python
# import numpy
# numpy.add.at(target, idx, vals)

import fastfunc

fastfunc.add.at(target, idx, vals)

# If you really only need _add_, you can use
# numpy.bincount(idx, weights=vals, minlength=target.shape[0])
```
to get a speed-up by a factor of 40.

![](https://nschloe.github.io/fastfunc/add.svg)

This is achieved by moving the operations to C++ using [pybind11](https://github.com/pybind/pybind11).

### Installation

fastfunc is [available from the Python Package
Index](https://pypi.org/project/fastfunc/), so simply do
```
pip install -U fastfunc
```
to install or upgrade.

### Testing

To run the fastfunc unit tests, check out this repository and type
```
pytest
```

### License

fastfunc is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
