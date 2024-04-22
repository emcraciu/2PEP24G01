"""Create thermometer that stores temp in K and can return any degrees"""

"""Create thermometer that stores temp in K and can return any degrees"""


class Thermometer:
    __temperature = 0
    degrees = "K"

    @property
    def temperature(self):
        if self.degrees == 'C':
            return f'{self.__temperature - 273.15} {self.degrees}'
        elif self.degrees == 'K':
            return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if self.degrees == 'K' and value >= 0:
            self.__temperature = value
        elif self.degrees == 'C' and value >= -273.15:
            self.__temperature = value + 273.15


t = Thermometer()
t.temperature = 10
t.degrees = "C"
t.temperature = 10
print(t.temperature)
