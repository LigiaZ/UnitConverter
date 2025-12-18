# Test script for check_temperature integration

from app import fahrenheit_to_celsius, check_temperature

# Test cases
test_cases = [
    (100, "F", "above 30°C"),
    (32, "F", "below 10°C"),
    (50, "F", "exactly 10°C"),
    (86, "F", "exactly 30°C"),
    (68, "F", "comfortable"),
    ("invalid", "F", "invalid input"),
]

for value, unit, description in test_cases:
    if unit == "F":
        try:
            celsius = fahrenheit_to_celsius(value)
            message = check_temperature(celsius)
            print(f"Input: {value}°F -> {celsius:.2f}°C, Message: {message} ({description})")
        except Exception as e:
            print(f"Error with {value}: {e}")
    else:
        message = check_temperature(value)
        print(f"Input: {value}, Message: {message} ({description})")