from machine import Pin, SoftI2C
import ssd1306
import time
import dht

#You can choose any other combination of I2C pins
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

# Initialize DHT11 sensor on GPIO 17
d = dht.DHT11(machine.Pin(17))


oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    d.measure()
    string_1 = f"Teplota: {d.temperature()}"
    string_2 = f"Vlhkost: {d.humidity()}%"
    oled.text('DHT11 sensor', 0, 0)
    oled.text(string_1, 0, 10)
    oled.text(string_2, 0, 20)

    oled.show()
    time.sleep(5)
    oled.fill(0)
