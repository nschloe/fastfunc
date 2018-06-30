# -*- coding: utf-8 -*-
#
import sys


def _operator_at(operator, a, k, vals):
    a_shape = a.shape

    k = _assert_native_byteorder(k)

    a = a.reshape(a.shape[0], -1)
    idx = k.reshape(-1)
    v = vals.reshape(idx.shape[0], -1)
    assert a.shape[1] == v.shape[1]

    operator(a, idx, v)

    a.reshape(a_shape)
    return


def _assert_native_byteorder(a):
    if a.dtype.byteorder == "=":
        return a

    sys_is_le = sys.byteorder == 'little'

    native_code = "<" if sys_is_le else ">"
    if a.dtype.byteorder == native_code:
        return a

    return a.byteswap().newbyteorder(native_code)
