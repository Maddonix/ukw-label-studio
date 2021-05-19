========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/ukw-label-studio/badge/?style=flat
    :target: https://ukw-label-studio.readthedocs.io/
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/Maddonix/ukw-label-studio.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/Maddonix/ukw-label-studio

.. |requires| image:: https://requires.io/github/Maddonix/ukw-label-studio/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/Maddonix/ukw-label-studio/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/Maddonix/ukw-label-studio/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/Maddonix/ukw-label-studio

.. |version| image:: https://img.shields.io/pypi/v/ukw-label-studio.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/ukw-label-studio

.. |wheel| image:: https://img.shields.io/pypi/wheel/ukw-label-studio.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/ukw-label-studio

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/ukw-label-studio.svg
    :alt: Supported versions
    :target: https://pypi.org/project/ukw-label-studio

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/ukw-label-studio.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/ukw-label-studio

.. |commits-since| image:: https://img.shields.io/github/commits-since/Maddonix/ukw-label-studio/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/Maddonix/ukw-label-studio/compare/v0.0.0...master



.. end-badges

Framework to hold configs and interaction methods for InExEn's labelling.

* Free software: MIT license

Installation
============

::

    pip install ukw-label-studio

You can also install the in-development version with::

    pip install https://github.com/Maddonix/ukw-label-studio/archive/master.zip


Documentation
=============


https://ukw-label-studio.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
