=======================
Modflow96 Scenario Generation and Data Processing
=======================

The ``msgdp`` package is a custom Python package for the Texas Advanced Computing Center `\(TACC\) <https://www.tacc.utexas.edu/>`_.

It was developed to facilitate running the MODFLOW 96 simulation on TACC HPC resources.

MODFLOW 96 is the MODFLOW is a three-dimensional finite-difference ground-water flow model hydrogeological simulation developed and maintained by the `USGS <http://water.usgs.gov/software/MODFLOW-96/>`_.

MODFLOW 96 is also the simulation used to validate all state approved groundwater availability models (GAMs) utilized by the Texas Water Development Board and its various partner organizations to draft legislation and define regulations for common pool resource management at a state-wide level.

The package contains multiple features including:

    - Specific makefile patches for building MODFLOW96 on the various TACC HPC environments
    - Preparation of input files and data sets required by the simulation
    - Generation of model cases to run en masse on the HPC systems
    - Generation of input files for parametric launcher and SLURM scripts
    - Post-processing of output data for analysis and export from the HPC systems
    - Utilities to facilitate populating a database with output
    - Utilities for scaffolding an `Adama <https://github.com/Arabidopsis-Information-Portal/adama>`_ adapter for the simulation data

To install the package with pip (PENDING):

    ``pip install msgdp``

To build the project from source, clone the repo, cd into the project dir and run:

    ``python setup.py sdist bdist_wheel``

Additional Usage Examples (TBD)
