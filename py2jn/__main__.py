from __future__ import print_function, absolute_import

import argparse
from py2jn.tools import python_to_notebook

description = """
Convert a literate Python script into a Jupyter Notebook
"""


def main():
    ap = argparse.ArgumentParser(description=description)
    ap.add_argument("source", help="python filename")
    ap.add_argument("destination", help="output notebook filename")
    args = ap.parse_args()
    # Process
    python_to_notebook(input_filename=args.source,
                       output_filename=args.destination)


if __name__ == '__main__':
    main()
