# -*- coding: utf-8 -*-
#
from _fastfunc import _subtract_at

from .helpers import _operator_at


def at(a, k, vals):
    _operator_at(_subtract_at, a, k, vals)
    return
