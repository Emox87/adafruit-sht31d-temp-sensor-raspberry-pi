# adafruit-sht31d-temp-sensor-raspberry-pi
Temperature sensor Adafruit SHT31D on raspberry pi

# Wiring and Library installation
https://learn.adafruit.com/adafruit-sht31-d-temperature-and-humidity-sensor-breakout/python-circuitpython

![alt text](https://cdn-learn.adafruit.com/assets/assets/000/058/803/original/adafruit_products_raspi_sht31d_i2c.jpg?1533843594 "Pi3 Wiring")

# Cli Commands order
1. sudo apt update && sudo apt upgrade
2. sudo pip3 install adafruit-circuitpython-sht31d
3. sudo raspi-config (make sure i2c interface its enabled)
4. i2cdetect -y 1 (check if the sensors its detected on the i2c interface)
5. python3 test.py (run the scripts and get the readings)
