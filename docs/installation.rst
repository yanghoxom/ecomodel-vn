Installation
============

Install for local development (private source)
----------------------------------------------

Clone the private project using an authorized GitHub account. EcoModel-VN has
not been published on conda-forge or PyPI.


Install editable package
------------------------

.. code-block:: console

    $ python -m pip install -e .

The Python import namespace is ecomodel_vn.


Install full environment for quickstart and examples
-----------------------------------------------------

In order to run the examples in the examples folder some additional packages to read
and write raster and vector data, as well as to plot these data are required.
We recommend using `rasterio <https://rasterio.readthedocs.io/>`__ raster data and
`geopandas <https://geopandas.org/>`__ for vector data.
A complete environment can be installed from the environment.yml file using:

.. code-block:: console

    $ conda env create -f environment.yml
