"""Utility functions."""

from __future__ import absolute_import, print_function

from io import StringIO
from nbformat.v3 import nbpy
import nbformat as nbf

from .reader import read


def convert(input_string, output_filename):
    """Convert a preprocessed string object into notebook file."""

    # Read using v3
    with StringIO(input_string) as fin:
        nb = nbpy.read(fin)
    # Write using the most recent version
    with open(output_filename, 'w') as fout:
        nbf.write(nb, fout, version=nbf.current_nbformat)


def python_to_notebook(input_filename, output_filename):
    """Convert the given python source file into a properly formatted
    notebook.
    """

    cvt = read(input_filename)
    convert(cvt, output_filename)
