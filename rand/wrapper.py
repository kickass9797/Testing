class Celsius:
    def __init__(self, temperature=0):
        self.__temperature = temperature

    @property
    def temperature(self):
        print("Getting Value")
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self.__temperature = value


temp = Celsius(23)
temp.temperature = 24
print(temp.temperature)
