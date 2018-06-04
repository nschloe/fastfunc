# -*- coding: utf-8 -*-
#


def _operator_at(operator, a, k, vals):
    a_shape = a.shape

    a = a.reshape(a.shape[0], -1)
    idx = k.reshape(-1)
    v = vals.reshape(idx.shape[0], -1)
    assert a.shape[1] == v.shape[1]

    operator(a, idx, v)

    a.reshape(a_shape)
    return
