"""
This exmaple demonstrates how to instantiate the
Adafruit BME280 Sensor using this library and just
the SPI bus and chip enable numbers.

Please note that Linux will mess with the system CE pins, so 
we are using an alternate pin for the Chip Enable line. This
library is more useful for using a SPI Device on a Bus other
than 0
"""

import board
import adafruit_bme280
from adafruit_extended_bus import ExtendedSPI as SPI

# Create library object using our Extended Bus I2C port
spi = SPI(1, 0)  # Device is /dev/spidev1.0
cs = digitalio.DigitalInOut(board.D5)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, cs)
print("\nTemperature: %0.1f C" % bme280.temperature)
