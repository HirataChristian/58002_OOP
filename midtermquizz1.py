class TemperatureConversion:
    def __init__(self, num, unit):
        self.num = num
        self.unit = unit.lower()

    def to_celsius(self):
        if self.unit == 'fahrenheit':
            return (self.num - 32) * 5/9
        elif self.unit == 'kelvin':
            return self.num - 273.15

    def to_fahrenheit(self):
        if self.unit == 'celsius':
            return (self.num * 9/5) + 32
        elif self.unit == 'kelvin':
            return (self.num * 9/5) - 459.67

    def to_kelvin(self):
        if self.unit == 'celsius':
            return self.num + 273.15
        elif self.unit == 'fahrenheit':
            return (self.num + 459.67) / 1.8

unit = input("Enter the unit of temperature to convert from (Celsius, Fahrenheit, or Kelvin): ").lower()
num = float(input("Enter the temperature in " + unit + ": "))
conv = TemperatureConversion(num, unit)

while True:
    choice = input("Enter the unit of temperature to convert to (Celsius, Fahrenheit, or Kelvin): ").lower()
    if choice == 'celsius':
        print(conv.to_celsius())
        break
    elif choice == 'fahrenheit':
        print(conv.to_fahrenheit())
        break
    elif choice == 'kelvin':
        print(conv.to_kelvin())
        break
    else:
        print("Invalid unit. Please choose Celsius, Fahrenheit, or Kelvin.")
