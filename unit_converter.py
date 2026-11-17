"""A very basic command-line unit converter."""

# Each category maps unit names to their value in a common base unit.
LENGTH = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0,
          "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.344}
WEIGHT = {"g": 1.0, "kg": 1000.0, "oz": 28.349523125, "lb": 453.59237}
TEMPERATURE = ["c", "f", "k"]


def convert_linear(value, from_unit, to_unit, table):
    """Convert using a table of factors relative to a base unit."""
    return value * table[from_unit] / table[to_unit]


def convert_temperature(value, from_unit, to_unit):
    """Convert between Celsius, Fahrenheit and Kelvin."""
    if from_unit == "f":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "k":
        celsius = value - 273.15
    else:
        celsius = value

    if to_unit == "f":
        return celsius * 9 / 5 + 32
    if to_unit == "k":
        return celsius + 273.15
    return celsius


def convert(value, from_unit, to_unit):
    """Convert value between any two supported units of the same kind."""
    from_unit, to_unit = from_unit.lower(), to_unit.lower()
    if from_unit in LENGTH and to_unit in LENGTH:
        return convert_linear(value, from_unit, to_unit, LENGTH)
    if from_unit in WEIGHT and to_unit in WEIGHT:
        return convert_linear(value, from_unit, to_unit, WEIGHT)
    if from_unit in TEMPERATURE and to_unit in TEMPERATURE:
        return convert_temperature(value, from_unit, to_unit)
    raise ValueError(f"Can't convert '{from_unit}' to '{to_unit}'")


def main():
    print("Simple Unit Converter")
    print("Length:      " + ", ".join(LENGTH))
    print("Weight:      " + ", ".join(WEIGHT))
    print("Temperature: " + ", ".join(TEMPERATURE))
    print("Example: 10 km mi   (type 'q' to quit)\n")

    while True:
        text = input("> ").strip()
        if text.lower() in ("q", "quit", "exit"):
            break
        try:
            value, from_unit, to_unit = text.split()
            result = convert(float(value), from_unit, to_unit)
            print(f"{value} {from_unit} = {result:.4g} {to_unit}")
        except ValueError as error:
            message = str(error)
            if "unpack" in message or "float" in message:
                message = "Please type: <number> <from unit> <to unit>"
            print(message)


if __name__ == "__main__":
    main()
