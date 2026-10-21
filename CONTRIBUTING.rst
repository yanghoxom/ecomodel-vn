Contributing to EcoModel-VN
===========================

EcoModel-VN is a private LEMBEM LAB research project.

Authorized collaborators can propose code, tests, methodological notes or
data-processing workflows through pull requests.

* Preserve reproducibility and document all scientific assumptions.
* Keep input-data provenance and validation clear.
* Never commit credentials, private data or unlicensed datasets.
* Retain upstream copyright and MIT licence notices.

Run tests locally:

.. code-block:: console

   python -m pip install -e ".[test]"
   python -m pytest tests -q

Contact: contact@lab.lembem.com
