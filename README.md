# py2jn

py2jn is a utility for converting Python scripts into Jupyter Notebooks.  Module-level multiline (triple quote) string literals are converted into markdown cells, and sections of code separated by such strings are converted into distinct code cells.


## Related Packages

This package is a fork of [sklam/py2nb](https://github.com/sklam/py2nb), which is no longer maintained. Of the numerous forks of this original project, the only ones that appear to include significant additional development are:
* [blueogive/py2nb](https://github.com/blueogive/py2nb)   Adds proper packaging including tests, and syntax for specifying raw notebook cells.
* [MarcusJones/py2jnb](https://github.com/MarcusJones/py2jnb)   Adds proper packaging including tests, and syntax for specifying notebook code cells. This package is available [via pip](https://pypi.org/project/py2jnb/).

There are also some independent packages with the same name and roughly the same
goals:
* [bjornaa/py2nb](https://github.com/bjornaa/py2nb)   Requires cell boundaries to be indicated via comments.
* [chicham/py2nb](https://github.com/chicham/py2nb)   Requires markdown, raw, and code cells to be indicated via comments.
* [williamjameshandley/py2nb](https://github.com/williamjameshandley/py2nb)   Requires markdown cells to be indicated via comments. This package is available [via pip](https://pypi.org/project/py2nb/).


## Requirements

The only requirement is [nbformat](https://github.com/jupyter/nbformat).  Under Ubuntu Linux 18.04, this requirement can be installed by the command
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

To execute the notebook do
```bash
  jupyter nbconvert --to=notebook --execute output.ipynb
```
and to convert to HTML do
```bash
  jupyter nbconvert --to=html output.ipynb
```


## Examples

See files `example.py` and `example.ipynb` in the `tests` directory.


## Contact

Bug reports can be submitted via the [GitHub Issues interface](https://github.com/bwohlberg/py2nb/issues).


## License

py2nb is distributed as open-source software under a BSD 3-Clause License (see the ``LICENSE`` file for details).
