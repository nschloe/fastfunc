from _fastfunc import _divide_at

from .helpers import _operator_at


def at(a, k, vals):
    _operator_at(_divide_at, a, k, vals)
    return
