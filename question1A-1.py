#I Sujan Rokad, 000882948, certify that this work is my own effort and that I have not allowed anyone else to copy from it.

"""
Author:                 Sujan Rokad
Authorship statement:   I, Sujan Rokad, 000882948, certify that this material is my original work. No other person's work has been used without due acknowledgement.
Purpose:                Determine if a given pH value is acidic, alkaline, or neutral.
"""

def determine_pH_category(pH):
    """
    Determines the pH category based on the provided pH value.

    Args:
        pH (float): The pH value to be categorized.

    Returns:
        str: A string indicating the pH category.
    """
    print("Running solution to question 1A...")

    if 7 < pH < 10:
        return "Alkali it is"
    elif pH >= 10:
        return "VERY Alkali it is"
    elif 4 < pH < 7:
        return "Acidic it is"
    elif pH <= 4:
        return "VERY Acidic it is"
    else:
        return "pH is 7 means Neutral"

# Get pH value from the user
pH = float(input("Enter a pH value: "))
result = determine_pH_category(pH)
print(result)
