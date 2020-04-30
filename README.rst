Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-python-extended_bus/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/extended_bus/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_Python_Extended_Bus/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_Python_Extended_Bus/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

Helper Library for Blinka to allow creating I2C and SPI busio objects by passing in the Bus ID.
This library is not compatible with CircuitPython and is intended to only be run on Linux devices.

Dependencies
=============
This driver depends on:

* `Adafruit Python <https://github.com/adafruit/Python>`_

Please ensure all dependencies are available on the Python filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://Python.org/libraries>`_.

Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-extended_bus/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-extended-bus

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-extended-bus

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-extended-bus

Usage Example
=============

.. code-block:: python

    from adafruit_extended_bus import ExtendedI2C as I2C
    import adafruit_bme280

    # Create library object using our Extended Bus I2C port
    i2c = I2C(1) # Device is /dev/i2c-1
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    print("\nTemperature: %0.1f C" % bme280.temperature)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_Python_Extended_Bus/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-Python-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
