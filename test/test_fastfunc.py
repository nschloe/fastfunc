# -*- coding: utf-8 -*-
#
import numpy

import fastfunc


def test_add():
    numpy.random.seed(123)

    a0 = numpy.zeros(10, dtype=int)
    k = numpy.random.randint(10, size=5)
    v = numpy.random.randint(7, size=5)
    numpy.add.at(a0, k, v)

    a1 = numpy.zeros(10, dtype=int)
    fastfunc.add_at(a1, k, v)

    assert numpy.all(a0 == a1)
    return


if __name__ == '__main__':
    test_add()
