# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main function to handle user input and perform conversions
def main():
    try:
        temperature = float(input("Enter the temperature: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature} degrees Celsius is equal to {converted_temp:.2f} degrees Fahrenheit.")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature} degrees Fahrenheit is equal to {converted_temp:.2f} degrees Celsius.")
        else:
            raise ValueError("Invalid unit. Please specify 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

