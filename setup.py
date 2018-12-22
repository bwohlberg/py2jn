#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from ast import parse


name = 'py2jn'
# See http://stackoverflow.com/questions/2058802
with open('py2jn/__init__.py') as f:
    version = parse(next(filter(
        lambda line: line.startswith('__version__'),
        f))).body[0].value.s

packages = [name]

longdesc = \
"""
py2jn is a small utility for converting Python scripts into Jupyter
Notebooks and convert module-level multiline (triple quote) string
literals into markdown cells.
"""

setup(
    name             = name,
    version          = version,
    packages         = packages,
    description      = 'py2jn: convert Python script to Jupyter Notebook',
    long_description = longdesc,
    keywords         = ['Jupyter Notebook'],
    platforms        = 'Any',
    license          = 'BSD',
    url              = 'https://github.com/bwohlberg/py2jn',
    author           = 'Siu Kwan Lam',
    author_email     = None,
    maintainer       = 'Brendt Wohlberg',
    maintainer_email = 'brendt@ieee.org',
    setup_requires   = [],
    tests_require    = ['pytest', 'pytest-runner'],
    install_requires = ['nbformat'],
    extras_require   = {
        'tests': ['pytest', 'pytest-runner']},
    classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Topic :: Utilities',
    ],
    zip_safe = True
)
