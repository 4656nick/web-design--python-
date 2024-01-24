import math


def calculate_area_for_cube(a: int) -> int:
    return 6 * a ** 2


def calculate_area_for_square(a: int) -> int:
    return a ** 2


def calculate_area_for_circle(radius: int) -> float:
    return math.pi * radius


def calculate_area_for_rectangle(a: int, b: int) -> int:
    return a * b


def calculate_area_for_triangle(height: int, b: int) -> float:
    return height * b / 2


def calculate_area_for_parallelogram(a: int, b: int, angle: int) -> float:
    return a * b * math.sin(angle)
