"""File to Classify a triangle"""
import math
from mybrand import my_brand
my_brand("SSW 567 HW 05-Static Code Analysis")


def classify_triangle(side_a,side_b,side_c):
    """Function to Classify a triangle"""
    # require that the input values be >= 0 and <= 200
    if side_a > 200 or side_b > 200 or side_c > 200:
        return 'InvalidInput'
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return 'InvalidInput'
    # Triangle Inequality Theorem:
    # the sum of any two sides must be strictly greater than the third side
    if not(((side_b + side_c) > side_a) and ((side_a + side_c) > side_b) and ((side_a + side_b) > side_c)):
        return 'NotATriangle'
    iso = False
    right = False
    if (math.isclose(side_a,side_b) and math.isclose(side_b,side_c) and math.isclose(side_a,side_c)):
        return 'Equilateral'
    if (math.isclose(side_a,side_b) or math.isclose(side_b,side_c) or math.isclose(side_a,side_c)):
        iso = True
    if (math.isclose(side_a**2 + side_b**2, side_c**2) or math.isclose(side_b**2 + side_c**2, side_a**2) or math.isclose(side_a**2 + side_c**2, side_b**2)):
        right = True
    if iso:
        if right:
            return "Isosceles and Right"
        return "Isosceles"
    if right:
        return "Scalene and Right"
    return "Scalene"

my_brand("SSW 567 HW 05-Static Code Analysis")
