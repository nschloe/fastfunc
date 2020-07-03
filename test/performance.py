import numpy

import fastfunc
import numpy_groupies
import perfplot

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


def numpy_groupies_aggregate_sum(data):
    a, i = data
    return numpy_groupies.aggregate(i, a, func="sum", size=m)


def numpy_bincount(data):
    a, i = data
    return numpy.bincount(i, weights=a, minlength=m)


def setup(n):
    a = numpy.random.rand(n)
    i = numpy.random.randint(0, m, n)
    return a, i


perfplot.show(
    setup=setup,
    kernels=[
        numpy_add_at,
        fastfunc_add_at,
        numpy_groupies_aggregate_sum,
        numpy_bincount,
    ],
    labels=[
        "numpy.add.at",
        "fastfunc.add.at",
        'numpy_groupies.aggregate("sum")',
        "numpy.bincount",
    ],
    n_range=[2 ** k for k in range(25)],
    logx=True,
    logy=True,
    xlabel="num additions",
)
