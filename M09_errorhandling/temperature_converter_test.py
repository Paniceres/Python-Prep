import unittest

class TemperatureConverter:
    def __init__(self, value, source_unit, target_unit):
        if source_unit not in [1, 2, 3] or target_unit not in [1, 2, 3]:
            raise ValueError("Unrecognized source or target unit. Try 1 for Kelvin, 2 for Celsius, or 3 for Fahrenheit.")
        
        self.value = value
        self.source_unit = source_unit
        self.target_unit = target_unit
    
    def convert_temperature(self):
        if self.source_unit == 1:  # Kelvin
            if self.target_unit == 3:  # Fahrenheit
                return self.value * 1.8 - 459.67
            elif self.target_unit == 2:  # Celsius
                return self.value - 273.15
        elif self.source_unit == 2:  # Celsius
            if self.target_unit == 1:  # Kelvin
                return self.value + 273.15
            elif self.target_unit == 3:  # Fahrenheit
                return self.value * 1.8 + 32
        elif self.source_unit == 3:  # Fahrenheit
            if self.target_unit == 1:  # Kelvin
                return (self.value + 459.67) * 5/9
            elif self.target_unit == 2:  # Celsius
                return (self.value - 32) * 5/9

        raise ValueError("Unrecognized source or target unit. Try 1 for Kelvin, 2 for Celsius, or 3 for Fahrenheit.")


class TestTemperatureConverter(unittest.TestCase):
    def test_invalid_creation(self):
        with self.assertRaises(ValueError):
            converter = TemperatureConverter(54, 4, 2)  # Invalid source unit (4)
        
        with self.assertRaises(ValueError):
            converter = TemperatureConverter(54, 2, 5)  # Invalid target unit (5)
    
    def test_valid_creation(self):
        converter = TemperatureConverter(54, 2, 3)
        self.assertEqual(converter.value, 54)
        self.assertEqual(converter.source_unit, 2)
        self.assertEqual(converter.target_unit, 3)
    
    def test_convert_temperature(self):
        converter = TemperatureConverter(54, 2, 3)
        converted_value = converter.convert_temperature()
        self.assertAlmostEqual(converted_value, 129.20, places=2)  # Assuming Fahrenheit to Celsius conversion
    
        converter = TemperatureConverter(100, 1, 2)
        converted_value = converter.convert_temperature()
        self.assertAlmostEqual(converted_value, -173.15, places=2)  # Assuming Kelvin to Celsius conversion

if __name__ == '__main__':
    unittest.main()
