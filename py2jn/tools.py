"""Utility functions."""

from __future__ import absolute_import, print_function

from io import BytesIO, StringIO
from nbformat.v3 import nbpy
import nbformat as nbf

from .reader import read_python


__all__ = ['py_string_to_nb_string', 'py_file_to_nb_string',
           'nb_string_to_notebook', 'write_notebook',
           'write_notebook_to_string', 'python_to_notebook']


def py_string_to_nb_string(str):
    """
    Read a string containing a regular Python script with special
    formatting, and perform preprocessing on it.  The result is a
    string that conforms to the IPython notebook version 3 Python
    script format.
    """

    return read_python(BytesIO(str.encode()))


def py_file_to_nb_string(filename):
    """
    Read a regular Python file with special formatting, and perform
    preprocessing on it.  The result is a string that conforms to the
    IPython notebook version 3 Python script format.
    """

    with open(filename, 'rb') as fin:
        ipy = read_python(fin)

    return ipy


def nb_string_to_notebook(str):
    """Convert a string representation of a notebook into a notebook
    object.
    """

    # Read using v3 of nbformat
    with StringIO(str) as fin:
        nb = nbpy.read(fin)

    return nb


def write_notebook(nb, filename):
    """Write a notebook object to a file."""

    # Write using the most recent version of nbformat
    with open(filename, 'w') as fout:
        nbf.write(nb, fout, version=nbf.current_nbformat)


def write_notebook_to_string(nb):
    """Write a notebook object to a string."""

    # Write using the most recent version of nbformat
    with StringIO('') as fout:
        nbf.write(nb, fout, version=nbf.current_nbformat)
        str = fout.getvalue()
    return str


def python_to_notebook(input_filename, output_filename):
    """Convert the given python source file into a properly formatted
    notebook.
    """

    nbstr = py_file_to_nb_string(input_filename)
    nb = nb_string_to_notebook(nbstr)
    write_notebook(nb, output_filename)
