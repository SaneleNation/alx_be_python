#This script prints a multiplication table based on a number the user inputs.

#The user inputs the number they want a multiplication table for.
number = int(input("Enter a number to see its multiplication table: "))

#Generate and print the multiplication table.
for y in range(1,11):
    z = number * y
    print(f"{number}*{y} = {z}")
