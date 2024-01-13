#I Sujan Rokad, 000882948, certify that this work is my own effort and that I have not allowed anyone else to copy from it.

"""
Author:                 Sujan Rokad
Authorship statement:   I, Sujan Rokad, 000882948, certify that this material is my original work. No other person's work has been used without due acknowledgement.
Purpose:                Determine the habitability of a planet based on its temperature.
"""

def determine_planet_habitability(temp):
    """
    Determines the habitability of a planet based on its temperature.

    Args:
        temp (float): The temperature of the planet.

    Returns:
        str: A string indicating the habitability status of the planet.
    """
    print("Running solution to question 1B...")

    if 0 < float(temp) < 21:
        return "Water can be present but neither Planet is habitable nor Crops can grow"
    elif 21 <= float(temp) < 32:
        return "Water can be present, Crops can grow, and Planet is considered habitable"
    elif 32 < float(temp) <= 100:
        return "Water can be present but neither Planet is habitable nor Crops can grow"
    else:
        return "Planet is not considered habitable"

# Get temperature from the user
temp = input("Enter temperature: ")
result = determine_planet_habitability(temp)
print(result)
