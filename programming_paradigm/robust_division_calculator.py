def safe_divide(numerator, denominator):
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform division and handle zero division error
        try:
            result = numerator / denominator
            print(f"The result of the division {result}")
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
        except ValueError:
            return "Error: Please enter numeric values only."

