"""Utility functions."""

from __future__ import absolute_import, print_function

from io import StringIO
from nbformat.v3 import nbpy
import nbformat as nbf

from .reader import py_string_to_ipy_string, py_file_to_ipy_string


__all__ = ['py_string_to_notebook', 'py_file_to_notebook',
           'write_notebook_to_string', 'python_to_notebook']



def py_string_to_notebook(str, nbver=None):
    """Convert a string representation of a regular Python script into
    a notebook object.
    """

    ipy = py_string_to_ipy_string(str)
    # Read using v3 of nbformat
    with StringIO(ipy) as fin:
        nb = nbpy.read(fin)

    # Convert to specific notebook version if specified
    if nbver is not None:
        nb = nbf.convert(nb, nbver)

    return nb


def py_file_to_notebook(filename, nbver=None):
    """Convert a Python file into a notebook object."""

    ipy = py_file_to_ipy_string(filename)
    # Read using v3 of nbformat
    with StringIO(ipy) as fin:
        nb = nbpy.read(fin)

    # Convert to specific notebook version if specified
    if nbver is not None:
        nb = nbf.convert(nb, nbver)

    return nb


def write_notebook(nb, filename, nbver=nbf.current_nbformat):
    """Write a notebook object to a file. Use the most recent version of
    nbformat by default."""

    with open(filename, 'w') as fout:
        nbf.write(nb, fout, version=nbver)


def write_notebook_to_string(nb, nbver=nbf.current_nbformat):
    """Write a notebook object to a string.  Use the most recent
    version of nbformat by default.
    """

    with StringIO('') as fout:
        nbf.write(nb, fout, version=nbver)
        str = fout.getvalue()
    return str


def python_to_notebook(input_filename, output_filename):
    """Convert the given python source file into a properly formatted
    notebook.
    """

    nb = py_file_to_notebook(input_filename)
    write_notebook(nb, output_filename)
