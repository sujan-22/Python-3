#I Sujan Rokad, 000882948, certify that this work is my own effort and that I have not allowed anyone else to copy from it.

"""
Author:                 Sujan Rokad
Authorship statement:   I, Sujan Rokad, 000882948, certify that this material is my original work. No other person's work has been used without due acknowledgement.
Purpose:                Run the solution to question 1B repeatedly until the user decides to quit.
"""

from Question1B import determine_planet_habitability

while True:
    print("Running solution to question 1B...")
    temp = input("Enter Temperature ('quit' to exit): ")

    if temp.lower() == "quit":
        break

    try:
        temp_float = float(temp)
        if 0 <= temp_float <= 100:
            answer = determine_planet_habitability(temp_float)
            print(answer)
        else:
            print("Input should be in degrees Celsius within the valid range.")
    except ValueError:
        print("Invalid input. Please enter a valid decimal number or 'quit'.")
