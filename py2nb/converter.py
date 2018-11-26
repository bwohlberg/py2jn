from __future__ import absolute_import, division, print_function

from nbformat.v3 import nbpy
import nbformat as nbf

from io import StringIO


def convert(input_string, output_filename):
    """Convert a preprocessed string object into notebook file."""

    # Read using v3
    with StringIO(input_string) as fin:
        nb = nbpy.read(fin)
    # Write using the most recent version
    with open(output_filename, 'w') as fout:
        nbf.write(nb, fout, version=nbf.current_nbformat)
