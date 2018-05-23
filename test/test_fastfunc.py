# -*- coding: utf-8 -*-
#
import numpy

import fastfunc


def test_add():
    numpy.random.seed(123)

    a0 = numpy.zeros(100, dtype=int)
    k = numpy.random.randint(0, 100, 1000)
    v = numpy.random.randint(0, 100, 1000)
    numpy.add.at(a0, k, v)

    a1 = numpy.zeros(100, dtype=int)
    fastfunc.add_at(a1, k, v)

    assert numpy.all(a0 == a1)
    return
