===========
EcoModel-VN
===========

**Environmental & Hydrological Modeling Research for Vietnam**

**Status:** In Development · Private

**Organization:** LEMBEM LAB — Laboratory for Emerging Media, Bio-informatics and Engineering Models

Overview
========

EcoModel-VN explores lightweight scientific models and reproducible workflows
for river-basin analysis, flood-susceptibility research and environmental
monitoring in Vietnam. The goal is accessible research for resource-limited
communities and laboratories.

Current capabilities
====================

The codebase currently supports terrain-based hydrological analysis:

* Digital Elevation Model (DEM) processing and flow directions
* River networks, drainage basins and upstream accumulation
* Stream ordering, tracing and watershed delineation
* Height Above Nearest Drainage (HAND) terrain indicators

These capabilities are research building blocks, **not** a validated
flood-forecasting or water-quality simulation product.

.. image:: docs/_static/hydrological_flows.png
   :alt: Hydrological terrain-analysis illustration from the original Deltares research code
   :width: 100%

Research roadmap
================

1. Adapt hydrological and terrain workflows to Vietnamese river basins.
2. Integrate environmental observations and evaluate water-quality modeling.
3. Study flood susceptibility, rainfall/runoff inputs and model validation.
4. Prepare public-benefit teaching materials and scientific outputs.

The repository remains private while development is underway.

Local development
=================

Python 3.11+ is recommended. Authorized collaborators can run:

.. code-block:: console

   git clone https://github.com/yanghoxom/ecomodel-vn.git
   cd ecomodel-vn
   python -m venv .venv
   # Activate the virtual environment for your operating system
   python -m pip install -e ".[test]"
   python -m pytest tests -q

Use the renamed Python package:

.. code-block:: python

   import ecomodel_vn

   # flow = ecomodel_vn.from_dem(data=elevation, nodata=nodata, transform=transform)

See examples/ and docs/ for hydrological workflows and API documentation.

Licensing & acknowledgements
============================

EcoModel-VN is based on the MIT-licensed hydrological analysis foundation
**PyFlwDir** created by **Deltares** (contributors include Dirk Eilander
and Willem van Verseveld). Its original copyright notice is preserved
unchanged in LICENSE. Original scientific images are retained with attribution.
This does not imply Deltares endorses EcoModel-VN.

Future EcoModel-VN modules and datasets may be licensed separately when released.

**Institute:** https://lab.lembem.com

**Contact:** contact@lembem.com
