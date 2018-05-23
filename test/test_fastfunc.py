# -*- coding: utf-8 -*-
#
import numpy

import fastfunc


def test_add_int():
    numpy.random.seed(123)

    a0 = numpy.zeros(10, dtype=int)
    k = numpy.random.randint(10, size=5)
    v = numpy.random.randint(7, size=5)
    numpy.add.at(a0, k, v)

    a1 = numpy.zeros(10, dtype=int)
    fastfunc.add.at(a1, k, v)

    assert numpy.all(a0 == a1)
    return


def test_add_float():
    numpy.random.seed(123)

    a0 = numpy.zeros(10)
    k = numpy.random.randint(10, size=5)
    v = numpy.random.rand(5)
    numpy.add.at(a0, k, v)

    a1 = numpy.zeros(10)
    fastfunc.add.at(a1, k, v)

    assert numpy.all(a0 == a1)
    return


def test_add_rows():
    numpy.random.seed(123)

    a0 = numpy.zeros((10, 3))
    k = numpy.random.randint(10, size=(5, 7))
    vals = numpy.random.rand(5, 7, 3)
    numpy.add.at(a0, k, vals)

    a1 = numpy.zeros((10, 3))
    fastfunc.add.at(a1, k, vals)

    assert numpy.all(a0 == a1)
    return


def test_add_multi():
    numpy.random.seed(123)

    a0 = numpy.zeros((10, 3, 4))
    k = numpy.random.randint(10, size=(5, 7))
    vals = numpy.random.rand(5, 7, 3, 4)
    numpy.add.at(a0, k, vals)

    a1 = numpy.zeros((10, 3, 4))
    fastfunc.add.at(a1, k, vals)

    assert numpy.all(a0 == a1)
    return


if __name__ == '__main__':
    test_add_rows()
