# SEED
 
**SEED**: **S**oftware for the **E**xtraction of **E**quations from **D**ata

## Table of contents
* [Introduction](#introduction)
* [Getting Started](#getting-started)
	* [Prerequisite](#prerequisite)
	* [Installing](#installing)
* [Usage](#usage)
	* [Running SEED](#running-SEED)
	* [Examples](#examples)
	* [Using your own data](#using-your-own-data)
* [Expansion](#expansion)
* [Lisense](#lisense)
* [Acknowledgments](#acknowledgments)

## Introduction
SEED is a software written in Python that provides a GUI for the extraction of governing differential equations from data. It does this by collating algorithms written for research into one overall package. Currently there are two different algorithms integrated into SEED:

* The Matlab SINDy code base written by the [Kutz Research Group](https://faculty.washington.edu/kutz/page26/) to accompany their paper [Discovering governing equations from data by sparse identification of nonlinear dynamical systems](https://www.pnas.org/content/113/15/3932.abstract)
* [PySINDy](https://github.com/luckystarufo/pySINDy), written by Yuying Liu, Yi Chu and Lianzong Wang, following on from the research of the Kutz Research group and other SINDy research

Any examples written for these sets of research have been edited for integration into SEED, but otherwise remain unedited. The ability to import a users own data to use with each algorithm has been added, to enable the analysis of further real world datasets.

SEED has an easy to use GUI to allow for researchers in many different fields to access the coded algorithms, although it is written in a way as to allow for the easy expansion of its capabilities. This enables users with a knowledge of programming to expand upon and improve the software.

## Getting Started

### Prerequisite
In order to run SINDy, Python 3.7 must be installed on your computer. If not, it can be downloaded and installed from [the Python website](https://www.python.org/downloads/release/python-377/).

In order to run the Matlab examples written by the Kutz Research Group, Matlab must be installed. This isn't required to run SEED however as Matlab has to be purchased. If the user would like to run the Matlab examples, the Matlab Engine for Python must be installed. This can be done by running these commands in the terminal or command line:

* Mac: 

> _cd /_
> 
> _cd Applications/MATLAB\_R2019b.app/extern/engines/python_
> <br />(**Change the name of your Matlab app to the version you have downloaded**)
> 
> _python3 setup.py install_

* Windows:

> _Coming soon_

### Installing
After downloading the source code from GitHub, save all of the files in a folder called _SEED_. This allows the programme to find the correct filepath to run the examples.

Before running SEED, it is vital to install the Python packages needed for the programme to run. This can be done by running these commands in the terminal or command line (**If running SEED through Jupyter Notebook, see the next paragraph!**):

* Mac: 

> _python3 -m pip install --user numpy scipy matplotlib pysindy findiff pytest pylint sphinx_

* Windows:

> _Coming soon_

SEED can also be run with Jupyter Notebook. As well as the _SEED.py_ file, _SEED.ipynb_ is available for those using Jupyter. The code is the same. Before running SEED in Jupyter Notebook, it is vital to install a few Python packages needed for the programme to run. This can be done by running these commands in the terminal or command line:

* Mac: 

> _python -m pip install --user pysindy findiff_

* Windows:

> _Coming soon_

## Usage

### Running SEED
To run SEED, open the Python IDLE (included with the Python 3.7 download) and open the file _SEED.py_. Click _Run > Run Module_ to run the software. If running SEED through Jupyter Notebook, open _SEED.ipynb_ in a Jupyter Notebook server and run all lines of code. 

The GUI will start up and will look like this:

![SEED GUI](GUI.png)

### Examples
Each algorithm that has been integrated with SEED comes with their own set of examples provided with the original research. The examples have been edited as to allow for easy integration into SEED. 

The data needed to run the third PySINDy example wasn't able to be included due to its size, but the generation script, _reaction\_diffusion.m_, is included in the _Algorithms > pySINDy > datasets_ directory. Open Matlab to run the script and generate the _reaction\_diffusion.mat_ data file.

### Using your own data
In order to use a users own data with the algorithms, the data must be saved as a _.csv_ file with one column of time series data, and up to three further columns containing the data for each recorded variable. The first row of the _.csv_ file must be the names of each variable.

The _.csv_ file must then be saved in the _SEED > Data_ folder in order to be found by the programme. There is an example of a data file in the _Data_ folder previously mentioned.

## Expansion
Coming soon

## Lisense
The MIT License is used for this software. For more information see: [License info](https://github.com/M-Vause/SEED/blob/master/LICENSE)

## Acknowledgments


