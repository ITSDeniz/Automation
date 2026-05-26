import math

def triangle_area(base, height):
    """Calculates the area of a triangle."""
    return 0.5 * base * height

def square_area(side):
    """Calculates the area of a square."""
    return side ** 2

if __name__ == "__main__":
    print(f"Triangle Area: {triangle_area(10, 5)}")
    print(f"Square Area: {square_area(4)}")