# -*- coding: utf-8 -*-
#
import numpy

# pylint: disable=import-error
import perfplot

import fastfunc


m = 100


def numpy_add_at(data):
    vals, idx = data
    a = numpy.zeros(m)
    numpy.add.at(a, idx, vals)
    return a


def fastfunc_add_at(data):
    vals, idx = data
    a = numpy.zeros(m)
    fastfunc.add.at(a, idx, vals)
    return a


perfplot.show(
    setup=lambda n: (numpy.random.rand(n), numpy.random.randint(m, size=n)),
    kernels=[numpy_add_at, fastfunc_add_at],
    labels=["numpy.add.at", "fastfunc.add.at"],
    n_range=[2 ** k for k in range(25)],
    logx=True,
    logy=True,
    xlabel="num additions",
)
