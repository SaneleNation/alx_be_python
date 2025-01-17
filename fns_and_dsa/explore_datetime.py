from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, number_of_days):
    future_date = current_date + timedelta(days=number_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"The date after {number_of_days} days will be: {formatted_future_date}")

def main():
    current_date = display_current_datetime()

    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, number_of_days)
    except ValueError:
        print("Invalid input. Please enter an integer value.")

if __name__ == "__main__":
    main()
