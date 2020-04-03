Welcome to PySINDy's documentation!
===================================

Python Sparse Identification of Nonlinear Dynamics

Description
--------------------
PySINDy is a Python package that implements the SINDy-family algorithms.
SINDy is short for "Sparse Identification of Nonlinear Dynamics", which
is a class of data-driven algorithms for system identification. This class
of algorithms are mainly developed by Steve Brunton and Nathan Kutz at the
University of Washington. Since then many variants arose, such as SINDy for
PDEs, implicit SINDy, parametric SINDy, Hybrid SINDy, SINDy with control, etc.
In PySINDy, we will (or we will try our best to) implement the majority of
the variants with friendly user interfaces and we will provide examples to
illustrate the usage.

Installation
--------------------
PySINDy requires numpy, scipy, matplotlib, findiff, pytest(for unittest), sphinx (for the
documentation). The code is compatible with Python 3.5 and Python 3.6. It can be
installed using pip or directly from the source code.

Installing via PIP
^^^^^^^^^^^^^^^^^^^^^^^^
Mac and Linux users can install pre-built binary packages using pip.
To install the package just type:
::

    pip install PySINDy

Installing from source
^^^^^^^^^^^^^^^^^^^^^^^^
The official distribution is on GitHub, and you can clone the repository using
::

    git clone https://github.com/luckystarufo/pySINDy

To install the package just type:
::

    python setup.py install



Developer's Guide
--------------------

.. toctree::
   :maxdepth: 1

   code
   contact
   contributing
   LICENSE

Tutorials
--------------------
We made some tutorial examples. Please refer to the official GitHub repository for the last
updates in the examples folder. Here the list of the exported tutorials:

- Tutorial 1 <a href="https://github.com/luckystarufo/pySINDy/blob/master/examples/example-1-sindy-vanderpol.ipynb">Van der Pol</a>
- Tutorial 2 <a href="https://github.com/luckystarufo/pySINDy/blob/master/examples/example-2-sindypde-burgers.ipynb">Burgers</a>
- Tutorial 3 <a href="https://github.com/luckystarufo/pySINDy/blob/master/examples/example-3-sindypde-reactiondiffusion.ipynb">Reaction-Diffusion</a>
- Tutorial 4 <a href="https://github.com/luckystarufo/pySINDy/blob/master/examples/example-4-isindy-subtilis_competence.ipynb">Biological network</a>
- more coming soon ...

References
--------------------
To implement the various versions of the SINDy algorithms we follow these works:

- Brunton, S. L., Proctor, J. L. & Kutz, J. N. Discovering governing equations from data by sparse identification of nonlinear dynamical systems. Proc. Natl Acad. Sci. 113, 3932–3937 (2016).
- Rudy, S. H., Brunton, S. L., Proctor, J. L. & Kutz, J. N. Data-driven discovery of partial differential equations. Sci. Adv. 3, e1602614 (2017).
- N.M. Mangan, S. L. Brunton, J. L. Proctor, J. N. Kutz, Inferring biological networks by sparse identification of nonlinear dynamics. IEEE Trans. Mol. Biol. Multi-Scale Commun. 2, 52–63 (2016).

Indices and tables
--------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
