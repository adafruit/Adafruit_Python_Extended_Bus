# The MIT License (MIT)
#
# Copyright (c) 2020 Melissa LeBlanc-Williams for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_extended_bus`
================================================================================

Helper Library for Blinka to allow creating I2C and SPI busio objects by passing in the Bus ID.
This library is not compatible with CircuitPython and is intended to only be run on Linux devices.

* Author(s): Melissa LeBlanc-Williams

"""

# imports
import threading

from os import path
from busio import I2C, SPI
from adafruit_blinka.microcontroller.generic_linux.i2c import I2C as _I2C
from adafruit_blinka.microcontroller.generic_linux.spi import SPI as _SPI

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_Python_Extended_Bus.git"


class ExtendedI2C(I2C):
    """Extended I2C is a busio extension that allows creating a compatible
    I2C object using the Bus ID number. The bus ID is the number at the end
    of /dev/i2c-# and you can find which I2C devices you have by typing
    ``ls /dev/i2c*``"""

    # pylint: disable=super-init-not-called
    def __init__(self, bus_id, frequency=400000):
        self.init(bus_id, frequency)

    # pylint: enable=super-init-not-called

    # pylint: disable=arguments-differ
    def init(self, bus_id, frequency):
        self.deinit()

        # Check if the file /dev/i2c-{bus_id} exists and error if not
        if not path.exists("/dev/i2c-{}".format(bus_id)):
            raise ValueError("No device found for /dev/i2c-{}".format(bus_id))
        # Attempt to open using _I2C
        self._i2c = _I2C(bus_id, mode=_I2C.MASTER, baudrate=frequency)

        self._lock = threading.RLock()

    # pylint: enable=arguments-differ


# pylint: disable=too-few-public-methods
class ExtendedSPI(SPI):
    """Extended SPI is a busio extension that allows creating a compatible
    SPI object using the Bus ID number. The bus ID is the numbers at the end
    of /dev/spidev#.# and you can find which SPI devices you have by typing
    ``ls /dev/spi*``"""

    # pylint: disable=invalid-name, redefined-builtin
    class Pin:
        """Fake Pin class"""

        def __init__(self, id):
            self.id = id

    # pylint: enable=invalid-name, redefined-builtin

    # pylint: disable=super-init-not-called
    def __init__(self, bus_id, chip_select):
        self.deinit()

        # Check if the file /dev/i2c-{bus_id} exists and error if not
        if not path.exists("/dev/spidev{}.{}".format(bus_id, chip_select)):
            raise ValueError(
                "No device found for /dev/spidev{}.{}".format(bus_id, chip_select)
            )

        self._spi = _SPI((bus_id, chip_select))
        # Pins aren't used in Linux, so we just use fake pins
        self._pins = (self.Pin(0), self.Pin(0), self.Pin(0))

    # pylint: enable=super-init-not-called


# pylint: enable=too-few-public-methods
