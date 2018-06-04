# -*- coding: utf-8 -*-
#
from __future__ import print_function

from .__about__ import (
    __author__,
    __author_email__,
    __copyright__,
    __license__,
    __version__,
    __maintainer__,
    __status__,
)

from . import add, subtract, multiply, divide

__all__ = [
    "__author__",
    "__author_email__",
    "__copyright__",
    "__license__",
    "__version__",
    "__maintainer__",
    "__status__",
    "add",
    "subtract",
    "multiply",
    "divide",
]

try:
    import pipdate
except ImportError:
    pass
else:
    if pipdate.needs_checking(__name__):
        print(pipdate.check(__name__, __version__), end="")
