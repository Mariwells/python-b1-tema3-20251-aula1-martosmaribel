# geometry.py


import math


def square_area(side_length: float) -> float:
    """
    Calculate the area of a square.

    Args:
    - side_length (float): the length of one side of the square.

    Returns:
    - float: the area of the square.
    """
    if isinstance(side_length, (int, float)):
        return side_length ** 2
    raise ValueError("side_length must be a number.")


def rectangle_area(base_length: float, height: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
    - base_length (float): the length of the base of the rectangle.
    - height (float): the height of the rectangle.

    Returns:
    - float: the area of the rectangle.
    """
    if isinstance(base_length, (int, float)) and isinstance(height, (int, float)):
        return base_length * height
    raise ValueError("base_length and height must be numbers.") 


def triangle_area(base_length: float, height: float) -> float:
    """
    Calculate the area of a triangle.

    Args:
    - base_length (float): the length of the base of the triangle.
    - height (float): the height of the triangle.

    Returns:
    - float: the area of the triangle.
    """
    if isinstance(base_length, (int, float)) and isinstance(height, (int, float)):
        return 0.5 * base_length * height
    raise ValueError("base_length and height must be numbers.") 


def circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
    - radius (float): the radius of the circle.

    Returns:
    - float: the area of the circle
    """
    if isinstance(radius, (int, float)):
        return math.pi * radius ** 2
    raise ValueError("radius must be a number.")
