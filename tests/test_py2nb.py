#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_py2nb
----------------------------------

Tests for `py2nb` module.
"""

import os
from tempfile import gettempdir
import pytest
from py2nb.__main__ import python_to_notebook


@pytest.fixture
def samplepy(fname='example.py'):
    return os.path.join('tests', fname)


@pytest.fixture
def sampleipynb(fname='example.ipynb'):
    return os.path.join('tests', fname)


def test_py2nb(samplepy, sampleipynb):
    tmpdir = gettempdir()
    python_to_notebook(input_filename=samplepy,
                       output_filename=os.path.join(tmpdir,
                                                    'py2nb_example.ipynb'))
    with open(os.path.join(tmpdir, 'py2nb_example.ipynb'), 'r') as outfileobj:
        outfile = outfileobj.read()
    with open(sampleipynb, 'r') as reffileobj:
        refile = reffileobj.read()
    assert outfile == refile
    os.remove(os.path.join(tmpdir, 'py2nb_example.ipynb'))
