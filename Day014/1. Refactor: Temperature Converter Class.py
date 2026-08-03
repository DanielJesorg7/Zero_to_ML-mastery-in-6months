class Temperature:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit.upper()

    def to_celsius(self):
        if self.unit == "C":
            return self.value
        elif self.unit == "F":
            return (self.value - 32) * 5 / 9
        elif self.unit == "K":
            return self.value - 273.15

    def to_fahrenheit(self):
        c = self.to_celsius()
        return (c * 9 / 5) + 32

    def to_kelvin(self):
        c = self.to_celsius()
        return c + 273.15

    def convert(self, to_unit):
        to_unit = to_unit.upper()
        if to_unit == "C":
            return self.to_celsius()
        elif to_unit == "F":
            return self.to_fahrenheit()
        elif to_unit == "K":
            return self.to_kelvin()
        else:
            raise ValueError("Invalid unit. Use 'C', 'F', or 'K'.")

# Example usage:
t = Temperature(25, "C")
print(t.convert("F"))  # Output: 77.0
