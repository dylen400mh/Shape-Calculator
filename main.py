from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle
from dimension import Dimension


def get_shape():
    while True:
        shape = input(
            "Please choose a 2D shape (rectangle, square, triangle, circle): ")
        if shape.lower() in ["rectangle", "square", "triangle", "circle"]:
            break
        else:
            print("Invalid option. Please try again.")
    return shape.lower()


print("This program calculates the area and perimeter of a shape of your choice.")
shape = get_shape()

if shape == "rectangle":
    length = Dimension.get_length()
    width = Dimension.get_width()
    rectangle = Rectangle(length, width)
    area = rectangle.get_area()
    perimeter = rectangle.get_perimeter()

elif shape == "square":
    length = Dimension.get_length()
    square = Square(length)
    area = square.get_area()
    perimeter = square.get_perimeter()

elif shape == "triangle":
    side1 = Dimension.get_side1()
    side2 = Dimension.get_side2()
    side3 = Dimension.get_side3()
    triangle = Triangle(side1, side2, side3)
    area = triangle.get_area()
    perimeter = triangle.get_perimeter()

elif shape == "circle":
    radius = Dimension.get_radius()
    circle = Circle(radius)
    area = circle.get_area()
    perimeter = circle.get_perimeter()

print(f"The area of the {shape} is: {round(area,2)}")
print(f"The perimeter of the {shape} is: {round(perimeter,2)}")
