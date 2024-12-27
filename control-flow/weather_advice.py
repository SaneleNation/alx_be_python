#This script is about asking the user the weather conditions and then recommending clothing based on the weather.


#The user inputs the type of weather condition.
weather = input("What's the weather like today? (sunny/rainy/cold): ")

#Clothing type that will be recommended based on user input and displays the results.
if "sunny" in weather:
    print("Wear a t-shirt and sunglasses.")

elif "rainy" in weather:
    print("Don't forget your umbrella and a raincoat.")

elif "cold" in weather:
    print("Make sure to wear a warm coat and a scarf.")

else :
    print("Sorry, I don't have recommendations for this weather.")

    
