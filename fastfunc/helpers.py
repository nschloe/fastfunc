# -*- coding: utf-8 -*-
#
import sys


def _operator_at(operator, a, k, vals):
    assert (
        k.shape == vals.shape[: len(k.shape)]
    ), "Shape mismatch! (target.shape = {}, index.shape = {}, values.shape = {}".format(
        a.shape, k.shape, vals.shape
    )

    assert (
        a.shape[1:] == vals.shape[len(k.shape) :]
    ), "Shape mismatch! (target.shape = {}, index.shape = {}, values.shape = {}".format(
        a.shape, k.shape, vals.shape
    )

    a_shape = a.shape

    # Never copy the target, a.
    _assert_native_byteorder(a)
    k = _copy_to_native_byteorder(k)
    vals = _copy_to_native_byteorder(vals)

    a = a.reshape(a.shape[0], -1)
    idx = k.reshape(-1)
    v = vals.reshape(idx.shape[0], -1)

    operator(a, idx, v)

    a.reshape(a_shape)
    return


def _assert_native_byteorder(a):
    native_code = {"little": "<", "big": ">"}[sys.byteorder]
    assert a.dtype.byteorder in ["=", "|", native_code]
    return


def _copy_to_native_byteorder(a):
    native_code = {"little": "<", "big": ">"}[sys.byteorder]
    if a.dtype.byteorder in ["=", "|", native_code]:
        return a
    return a.byteswap().newbyteorder(native_code)
