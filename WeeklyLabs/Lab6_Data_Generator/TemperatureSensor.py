import random
import matplotlib.pyplot as plt

class TemperatureSensor:
    # class that takes min and max values in the constructor to specify the temp. range
    # by default it's set to typical range for a server room (18C to 21C)
    def __init__(self, base_min=18, base_max=21):
        self.base_min = base_min
        self.base_max = base_max

    def _generate_normalized_value(self):
        return random.random()  # generates random value between 0 and 1

    @property
    def temperature(self):
        # property that uses normalized value to calculate the temp. within the specified range
        # uses provided formula 'y= mx + c', where 'm' is temperature_range, 'x' is normalized
        # value, and c is 'base_min')
        normalized_value = self._generate_normalized_value()
        # transform the normalized value to the temp. range
        temperature_range = self.base_max - self.base_min
        temperature = normalized_value * temperature_range + self.base_min
        return temperature

# create instance of 'TemperatureSensor and generate series of temp. values
if __name__ == "__main__":
    sensor = TemperatureSensor()
    number_of_values = 500
    temperatures = [sensor.temperature for _ in range(number_of_values)]
    plt.plot(temperatures)
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title('Server Room Temperature Monitoring')
    plt.show()