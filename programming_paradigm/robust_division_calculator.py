def safe_divide(numerator,denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator != 0 :
            results = numerator / denominator
            print(f"The results of the division is {results}")
        else:
            raise ZeroDivisionError
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
