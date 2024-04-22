"""Create thermometer that stores temp in K and can return any degrees"""

class Thermometer:
    _temperature = 0
    degrees = "K"


t = Thermometer()
t.temperature = 10
t.degrees = "C"
print(t.temperature)
