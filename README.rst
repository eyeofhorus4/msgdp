=======================
Modflow96 Scenario Generation and Data Processing
=======================
-----------------------

-----------------------

The ``msgdp`` package is a custom Python package for the Texas Advanced Computing Center.

It was developed to facilitate running the MODFLOW 96 simulation on TACC HPC resources.

MODFLOW 96 is a Hydrogeological simulation developed and maintained by the `USGS <http://water.usgs.gov/software/MODFLOW-96/>`.

The package contains multiple features including:
    - Specific build patches for building MODFLOW96 in the TACC HPC environments
    - Preparation of input files and data required by the simulation
    - Generation of model cases to run en masse on the HPC systems
    - Generation of input files for parametric launcher and SLURM
    - Post-processing of output data for analysis and export from the HPC systems

----

To build the project from source, clone the repo, cd into the project dir and run:

    ``python setup.py sdist bdist_wheel``


Additional Usage Examples (TBD)


----
