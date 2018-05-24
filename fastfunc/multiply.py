# -*- coding: utf-8 -*-
#
from _fastfunc import _multiply_at

from .helpers import _operator_at


def at(a, k, vals):
    _operator_at(_multiply_at, a, k, vals)
    return
