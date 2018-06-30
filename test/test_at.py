# -*- coding: utf-8 -*-
#
import numpy
import pytest

import fastfunc


@pytest.mark.parametrize(
    "dtype_data",
    [
        int,
        float,
        numpy.int8,
        numpy.int16,
        numpy.int32,
        numpy.int64,
        numpy.uint8,
        numpy.uint16,
        numpy.uint32,
        numpy.uint64,
        # numpy.float16: not workingm has no C++ equivalent
        numpy.float32,
        numpy.float64,
        # numpy.dtype(">i4"): not working, byte order in target must be native
        numpy.dtype("<i4"),
    ],
)
@pytest.mark.parametrize(
    "dtype_idx",
    [
        int,
        numpy.int8,
        numpy.int16,
        numpy.int32,
        numpy.int64,
        numpy.uint8,
        numpy.uint16,
        numpy.uint32,
        numpy.uint64,
        numpy.dtype(">i4"),
        numpy.dtype("<i4"),
    ],
)
@pytest.mark.parametrize(
    "numpy_fun, fastfunc_fun",
    [
        (numpy.add.at, fastfunc.add.at),
        (numpy.subtract.at, fastfunc.subtract.at),
        (numpy.multiply.at, fastfunc.multiply.at),
        (numpy.divide.at, fastfunc.divide.at),
    ],
)
def test_dtypes(dtype_data, dtype_idx, numpy_fun, fastfunc_fun):
    numpy.random.seed(123)

    a0 = numpy.zeros(10, dtype=dtype_data)
    k = numpy.random.randint(10, size=5).astype(dtype_idx)
    v = (17 * numpy.random.rand(5)).astype(dtype_data)
    numpy_fun(a0, k, v)

    a1 = numpy.zeros(10, dtype=dtype_data)
    fastfunc_fun(a1, k, v)

    print(a0)
    print(a1)
    assert numpy.all(a0 == a1)
    return


@pytest.mark.parametrize(
    "numpy_fun, fastfunc_fun",
    [
        (numpy.add.at, fastfunc.add.at),
        (numpy.subtract.at, fastfunc.subtract.at),
        (numpy.multiply.at, fastfunc.multiply.at),
        (numpy.divide.at, fastfunc.divide.at),
    ],
)
def test_rows(numpy_fun, fastfunc_fun):
    numpy.random.seed(123)

    a0 = numpy.zeros((10, 3))
    k = numpy.random.randint(10, size=(5, 7))
    vals = numpy.random.rand(5, 7, 3)
    numpy_fun(a0, k, vals)

    a1 = numpy.zeros((10, 3))
    fastfunc_fun(a1, k, vals)

    assert numpy.all(a0 == a1)
    return


@pytest.mark.parametrize(
    "numpy_fun, fastfunc_fun",
    [
        (numpy.add.at, fastfunc.add.at),
        (numpy.subtract.at, fastfunc.subtract.at),
        (numpy.multiply.at, fastfunc.multiply.at),
        (numpy.divide.at, fastfunc.divide.at),
    ],
)
def test_multi(numpy_fun, fastfunc_fun):
    numpy.random.seed(123)

    a0 = numpy.zeros((10, 3, 4))
    k = numpy.random.randint(10, size=(5, 7))
    vals = numpy.random.rand(5, 7, 3, 4)
    numpy_fun(a0, k, vals)

    a1 = numpy.zeros((10, 3, 4))
    fastfunc_fun(a1, k, vals)

    assert numpy.all(a0 == a1)
    return


if __name__ == "__main__":
    test_rows(numpy.add.at, fastfunc.add.at)
