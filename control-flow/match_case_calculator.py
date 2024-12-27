#This calculator will prompt the user to enter two numbers and select an operation,then perform the calculation and display the results.


#User inputs two numbers and a operation.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose operatin(+,-,*,/) ")

#Perform the calculation using Match Case.
match operation :
    case "+":
        print("The result is",num1 + num2,".")
    case "-":
        print("The result is",num1 - num2,".")
    case "*":
        print("The result is",num1 * num2,".")
    case "/":
        if num2 != 0:
            print("The results is",num1 / num2,".")
        else:
            print("Cannot divide by zero")
    case _:
        print("Not a operation sign") 
