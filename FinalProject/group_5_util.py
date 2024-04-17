import random

class TemperatureGenerator:
    def __init__(self, base_min=18, base_max=21):
        self.base_min = base_min
        self.base_max = base_max

    def _generate_normalized_value(self):
        return random.random()

    @property
    def temperature(self):
        normalized_value = self._generate_normalized_value()
        temperature_range = self.base_max - self.base_min
        temperature = normalized_value * temperature_range + self.base_min
        return temperature

def create_data():
    temperature_sensor = TemperatureGenerator()
    data = {
        'temperature': temperature_sensor.temperature,
        'humidity': random.randint(40, 60),
        'pressure': random.randint(1000, 1020)
    }
    return data