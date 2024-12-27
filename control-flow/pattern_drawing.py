#This script draws a square pattern of asteriks based a value a user enters.

#User inputs the size of the pattern.
intenger = int(input("Enter the size of the pattern: "))
row = 0

#Use the given value to draw the pattern
while row < intenger:
    for col in range(intenger):
        print("*", end="")
    print()  # Move to the next line after finishing the row
    row += 1  # Increment the row counter
