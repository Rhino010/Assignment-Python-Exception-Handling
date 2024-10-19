# Objective: The aim of this assignment is to enhance your understanding of exception 
# handling by creating a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

# Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.

# Task 2: Temperature Conversion Write a function that converts the Fahrenheit 
# temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

# Use a try block to catch any potential errors during the conversion process. 
# What happens if they type out "thirty" instead of doing 30?

# Task 3: User Experience Implement an else block that prints 
# the converted temperature in a user-friendly format. 

# Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

# Task 4: Finally Add a finally block that thanks the user for using the weather 
# forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.


while True:
    try:
        temp_input = input("Please enter the temperature in Fahrenheit you wish to convert: \n")
        def temp_conversion(temp):
            value_convert = float(temp)
            cel_convert = (value_convert - 32) * 5 / 9
            return cel_convert
             
        result = temp_conversion(temp_input)
        
    except ValueError:
        print("Be sure to enter numerical values only. Try again please.")

    else:
        print(f"The celsius conversion of the temperature you entered is {result:.2f} degrees Celsius.\n")

    finally:
        print("Thank you for using the Celsius Conversion tool! We hope you found this useful.")

        
    continue_input = input("Would you like to continue working with this program? (yes/no)").lower()
    if continue_input != 'yes':
        break
# calls the function using an input from the user as the temperature passed through the code block



     