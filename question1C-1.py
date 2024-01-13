#I Sujan Rokad, 000882948, certify that this work is my own effort and that I have not allowed anyone else to copy from it.

"""
Author:                 Sujan Rokad
Authorship statement:   I, Sujan Rokad, 000882948, certify that this material is my original work. No other person's work has been used without due acknowledgement.
Purpose:                Determine the type of triangle based on its side lengths.
"""

def determine_triangle_type(side1, side2, side3):
    """
    Determines the type of triangle based on its side lengths.

    Args:
        side1 (int): Length of side 1.
        side2 (int): Length of side 2.
        side3 (int): Length of side 3.

    Returns:
        str: A string indicating the type of the triangle.
    """
    print("Running solution to question 1C...")

    if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
        if side1 == side2 == side3:
            return "Triangle is valid and Equilateral it is"
        elif side1 == side2 or side2 == side3 or side1 == side3:
            return "Triangle is valid and Isosceles it is"
        elif side1 != side2 and side2 != side3 and side1 != side3:
            return "Triangle is valid and Scalene it is"
    return "Triangle is not valid"

# Get side lengths from the user
side1 = int(input("Enter side 1 value: "))
side2 = int(input("Enter side 2 value: "))
side3 = int(input("Enter side 3 value: "))
result = determine_triangle_type(side1, side2, side3)
print(result)
