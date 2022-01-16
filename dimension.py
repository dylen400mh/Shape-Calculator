class Dimension:

    def get_length():
        while True:
            length = input("Enter the length: ")
            if not is_float(length):
                print("Input must be a number. Please try again.")
            elif float(length) <= 0:
                print("The length must be greater than 0. Please try again.")
            else:
                break
        return float(length)

    def get_width():
        while True:
            width = input("Enter the width: ")
            if not is_float(width):
                print("Input must be a number. Please try again.")
            elif float(width) <= 0:
                print("The width must be greater than 0. Please try again.")
            else:
                break
        return float(width)

    def get_side1():
        while True:
            side1 = input(f"Enter side length #1: ")
            if not is_float(side1):
                print("Input must be a number. Please try again.")
            elif float(side1) <= 0:
                print("The side length must be greater than 0. Please try again.")
            else:
                break
        return float(side1)

    def get_side2():
        while True:
            side2 = input(f"Enter side length #2: ")
            if not is_float(side2):
                print("Input must be a number. Please try again.")
            elif float(side2) <= 0:
                print("The side length must be greater than 0. Please try again.")
            else:
                break
        return float(side2)

    def get_side3():
        while True:
            side3 = input(f"Enter side length #3: ")
            if not is_float(side3):
                print("Input must be a number. Please try again.")
            elif float(side3) <= 0:
                print("The side length must be greater than 0. Please try again.")
            else:
                break
        return float(side3)

    def get_radius():
        while True:
            radius = input("Enter the radius: ")
            if not is_float(radius):
                print("Input must be a number. Please try again.")
            elif float(radius) <= 0:
                print("The radius must be greater than 0. Please try again.")
            else:
                break
        return float(radius)


def is_float(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
