# 1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is, area = (1/2)*base*height
print("\nExercise 1\n")

def calculate_area(base, height):
    """
    This function takes two parameters to Calculate the area of a triangle
    :param base: Base of triangle
    :param height: Height of triangle
    :return: Area of a shape
    """
    area = (1/2) * base * height
    return area

# 2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is, rectangle area=length*width
print("\nExercise 2\n")

def calculate_area2(dimension1, dimension2, shape="triangle"):
    """
    :param dimension1: In case of triangle it is "base", For rectangle it is "length".
    :param dimension2: In case of triangle it is "height", For rectangle it is "width".
    :param shape: Either "triangle" or "rectangle"
    :return: Area of a shape
    """
    if shape == "triangle":
        area = (1 / 2) * dimension1 * dimension2 # Triangle area is: 1/2(Base*Height)
        return area
    elif shape == "rectangle":
        area = dimension1 * dimension2 # Rectangle area is: Length*Width
        return area
    else:
        print("Error: Input must be 'triangle' or 'rectangle'")
        return None # if user didn't supply "triangle" or "rectangle" as shape then return none

# 3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# *
# **
# ***
# if input is 4 then it should print
# *
# **
# ***
# ****
print("\nExercise 3\n")

def print_pattern(num=5):
    """
    :param num: Integer number representing number of lines
    to be printed in a pattern. If num=3 it will print,
      *
      **
      ***
    If num=4, it will print,
      *
      **
      ***
      ****
    Default value for num is 5. So if function caller doesn't
    supply the input number then it will assume it to be 5
    :return: None
    """
    for i in range(1, num + 1):
        s=''
        for j in range(i):
            s += '*'
        print(s)


def print_pattern_pro(num=5):
    for i in range(1, num +1):
        print("*" * i)

