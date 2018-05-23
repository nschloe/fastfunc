# -*- coding: utf-8 -*-
#
import os
import codecs

from setuptools import setup, Extension, find_packages


# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, 'fastfunc', '__about__.py'), 'rb') as f:
    # pylint: disable=exec-used
    exec(f.read(), about)


# pylint: disable=too-few-public-methods
class get_pybind_include(object):
    '''Helper class to determine the pybind11 include path
    The purpose of this class is to postpone importing pybind11
    until it is actually installed, so that the ``get_include()``
    method can be invoked.
    '''
    def __init__(self, user=False):
        self.user = user

    def __str__(self):
        import pybind11
        return pybind11.get_include(self.user)


def read(fname):
    return codecs.open(os.path.join(base_dir, fname), encoding='utf-8').read()


ext_modules = [Extension(
    '_fastfunc',
    [
        'src/pybind11.cpp',
    ],
    language='c++',
    include_dirs=[
        # '/usr/include/eigen3/',
        # Path to pybind11 headers
        get_pybind_include(),
        get_pybind_include(user=True)
        ],
    libraries=[],
    # extra_compile_args=['-std=c++11']
    )]


setup(
    name='fastfunc',
    packages=find_packages(),
    ext_modules=ext_modules,
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    description=('Fast numpy ufunc operations'),
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/nschloe/fastfunc',
    license=about['__license__'],
    platforms='any',
    install_requires=[
        'numpy',
        'pipdate',
        'pybind11',
        ],
    classifiers=[
        about['__status__'],
        about['__license__'],
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries',
        ]
    )
