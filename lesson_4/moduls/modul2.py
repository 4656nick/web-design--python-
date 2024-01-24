import math


def calculate_volume_for_cube(a: int) -> int:
    return a ** 3


def calculate_volume_for_cylinder(radius: int, height: int) -> int:
    return math.pi * radius ** 2 * height


def calculate_volume_for_circle(radius: int) -> float:
    return 4 / 3 * math.pi * radius ** 3


def calculate_volume_for_rectangle(a: int, b: int, c: int) -> int:
    return a * b * c


def calculate_volume_for_pyramid(height: int, b: int) -> float:
    return height * b ** 2 / 3


def calculate_volume_for_parallelogram(a: int, b: int, c: int, ab: int, ac: int) -> float:
    return a * b * c * math.sin(ab) * math.sin(ac)
