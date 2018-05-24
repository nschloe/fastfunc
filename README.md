# fastfunc

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/fastfunc/master.svg)](https://circleci.com/gh/nschloe/fastfunc/tree/master)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/fastfunc.svg)](https://codecov.io/gh/nschloe/fastfunc)
[![Codacy grade](https://img.shields.io/codacy/grade/78fcd6e5db834f6ead92fcc35e1f7e5f.svg)](https://app.codacy.com/app/nschloe/fastfunc/dashboard)
[![speedy](https://img.shields.io/badge/speedy-gonzales-ff69b4.svg)](https://github.com/nschloe/fastfunc)
[![PyPi Version](https://img.shields.io/pypi/v/fastfunc.svg)](https://pypi.org/project/fastfunc)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/fastfunc.svg?logo=github&label=Stars)](https://github.com/nschloe/fastfunc)

[NumPy's own ufunc
operations](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ufunc.at.html)
are handy, but can be quite slow.  Use `fastfunc` as a drop-in replacement
```python
# import numpy
# numpy.add.at(target, idx, vals)

import fastfunc
fastfunc.add.at(target, idx, vals)
```
to get a speed-up by a factor of 40.

![](https://nschloe.github.io/fastfunc/add.png)

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

### Distribution
To create a new release

1. bump the `__version__` number,

2. publish to PyPi and tag on GitHub:
    ```
    $ make publish
    ```

### License

fastfunc is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
