# -*- coding: utf-8 -*-
#
import os
import codecs
import pybind11
import sys

import setuptools
from setuptools.command.build_ext import build_ext
from setuptools import setup, Extension, find_packages


# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, "fastfunc", "__about__.py"), "rb") as f:
    exec(f.read(), about)


class get_pybind_include(object):
    """Helper class to determine the pybind11 include path
    The purpose of this class is to postpone importing pybind11
    until it is actually installed, so that the ``get_include()``
    method can be invoked.
    """

    def __init__(self, user=False):
        self.user = user

    def __str__(self):
        return pybind11.get_include(self.user)


def read(fname):
    return codecs.open(os.path.join(base_dir, fname), encoding="utf-8").read()


# <https://github.com/pybind/python_example/blob/master/setup.py>
# As of Python 3.6, CCompiler has a `has_flag` method.
# cf http://bugs.python.org/issue26689
def has_flag(compiler, flagname):
    """Return a boolean indicating whether a flag name is supported on the specified
    compiler.
    """
    import tempfile

    with tempfile.NamedTemporaryFile("w", suffix=".cpp") as f:
        f.write("int main (int argc, char **argv) { return 0; }")
        try:
            compiler.compile([f.name], extra_postargs=[flagname])
        except setuptools.distutils.errors.CompileError:
            return False
    return True


# <https://github.com/pybind/python_example/blob/master/setup.py>
def cpp_flag(compiler):
    """Return the -std=c++[11/14] compiler flag.
    The c++14 is prefered over c++11 (when it is available).
    """
    if has_flag(compiler, "-std=c++14"):
        return "-std=c++14"
    elif has_flag(compiler, "-std=c++11"):
        return "-std=c++11"
    else:
        raise RuntimeError(
            "Unsupported compiler -- at least C++11 support " "is needed!"
        )


# <https://github.com/pybind/python_example/blob/master/setup.py>
class BuildExt(build_ext):
    """A custom build extension for adding compiler-specific options."""

    c_opts = {"msvc": ["/EHsc"], "unix": []}

    if sys.platform == "darwin":
        c_opts["unix"] += ["-stdlib=libc++", "-mmacosx-version-min=10.7"]

    def build_extensions(self):
        ct = self.compiler.compiler_type
        opts = self.c_opts.get(ct, [])
        if ct == "unix":
            opts.append('-DVERSION_INFO="%s"' % self.distribution.get_version())
            opts.append(cpp_flag(self.compiler))
            if has_flag(self.compiler, "-fvisibility=hidden"):
                opts.append("-fvisibility=hidden")
        elif ct == "msvc":
            opts.append('/DVERSION_INFO=\\"%s\\"' % self.distribution.get_version())
        for ext in self.extensions:
            ext.extra_compile_args = opts
        build_ext.build_extensions(self)


ext_modules = [
    Extension(
        "_fastfunc",
        ["src/pybind11.cpp"],
        language="c++",
        include_dirs=[
            # Path to pybind11 headers
            get_pybind_include(),
            get_pybind_include(user=True),
        ],
    )
]


setup(
    name="fastfunc",
    packages=find_packages(),
    ext_modules=ext_modules,
    #
    # <https://github.com/pybind/python_example/blob/master/setup.py>
    cmdclass={"build_ext": BuildExt},
    zip_safe=False,
    #
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    description=("Fast numpy ufunc operations"),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/nschloe/fastfunc",
    license=about["__license__"],
    platforms="any",
    install_requires=["numpy", "pybind11>=2.2"],
    setup_requires=["pybind11>=2.2"],
    classifiers=[
        about["__status__"],
        about["__license__"],
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
    ],
)
