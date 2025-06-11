FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if __name__ == "__main__":
    try: 
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        if unit == "C":
            result = convert_to_fahrenheit(temp)
            print(f"{result:.2f}°F ")
        elif unit.upper() == "F":
            result = convert_to_celsius(temp)
            print(f"{result:.2f}°C")
        else:
            print("Invalid unit. Please enter a valid unit C/F")
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
