# py2nb

py2nb is a utility for converting Python scripts into Jupyter notebooks.
Module-level multiline (triple quote) string literals are converted
into markdown cells, and sections of code separated by such strings are
converted into distinct code cells.


## Requirements

The only requirement is [nbformat](https://github.com/jupyter/nbformat).
Under Ubuntu Linux 18.04, this requirement can be installed by the command
```bash
  sudo apt-get install python-nbformat
```
or
```bash
sudo apt-get install python3-nbformat
```
for Python 2 or 3 respectively. It can also be installed via `pip`, e.g.
```bash
sudo -H pip install nbformat
```


## Installation

From the package root directory do
```bash
python setup.py install
```

## Usage

To convert a Python script into a Jypyter notebook do
```bash
python -m py2nb input.py output.ipynb
```

## Examples

See files `example.py` and `example.ipynb` in the `tests` directory.





# PY2NB: Python To Notebook Converter

This is a small utility for turning python scripts into jupyter notebooks and
convert module-level multiline (triple quote) string literals into markdown
cells.

## Why?

I wanted a tool to create user examples that can be executed as normal python
scripts so that they can be copy-and-pasted easily and can be rendered as
notebook for better readability (e.g nice styling, results embedded).

Also,

* Notebooks are nice to look at but slow to write
* Notebooks does not play well with version control


## Install

```bash
python setup.py install
```


## Usage


To convert a python script into a notebook do
```bash

python -m py2nb input.py output.ipynb
```

To execute the notebook do
```bash
jupyter nbconvert --to=notebook --execute output.ipynb
```
and to convert to HTML do
```bash
jupyter nbconvert --to=html output.ipynb
```


## Contact

Bug reports can be submitted via the [GitHub Issues interface](https://github.com/bwohlberg/py2nb/issues).



## License

py2nb is distributed as open-source software under a BSD 3-Clause License (see the ``LICENSE`` file for details).
