"""
This exmaple demonstrates how to instantiate the
Adafruit BME280 Sensor using this library and just
the I2C bus number.
"""

from adafruit_extended_bus import ExtendedI2C as I2C
import adafruit_bme280

# Create library object using our Extended Bus I2C port
i2c = I2C(1)  # Device is /dev/i2c-1
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
print("\nTemperature: %0.1f C" % bme280.temperature)
