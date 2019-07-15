from _fastfunc import _add_at

from .helpers import _operator_at


def at(a, k, vals):
    _operator_at(_add_at, a, k, vals)
    return
