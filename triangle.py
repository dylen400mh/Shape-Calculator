import math


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.semi_perimeter = (self.side1 + self.side2 + self.side3) / 2

    def get_area(self):
        try:
            return math.sqrt(self.semi_perimeter *
                             (self.semi_perimeter - self.side1) *
                             (self.semi_perimeter - self.side2) *
                             (self.semi_perimeter - self.side3))
        except ValueError:
            print("Invalid triangle. Restart the program to try again.")
            quit()

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3
