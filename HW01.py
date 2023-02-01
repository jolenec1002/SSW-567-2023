from mybrand import my_brand
import math
my_brand("SSW 567 HW 01 Testing Triangle Classificaiton")

def classify_triangle(a,b,c):
    if (a == 0) or (b == 0) or (c == 0):
        return "Not a triangle"
    if (a < 0) or (b < 0) or (c < 0):
        return "Not a triangle"
    if (a == b) and (b == c) and (a == c):
        return "Equilateral"
    if (a == b) or (b == c) or (a == c):
        if (round(a**2, 10) + round(b**2, 10) == round(c**2,10)):
            return "Isosceles and Right"
        else:
            return "Isosceles"
    else:
        if (round(a**2, 10) + round(b**2, 10) == round(c**2,10)):
            return "Scalene and Right"
        else:
            return "Scalene"

def main():
    print("")
    print("Sides: 1,1,1 is " + classify_triangle(1,1,1))
    print("Sides: 1,1,2 is " + classify_triangle(1,1,2))
    print("Sides: 1,1,sqrt(2) is " + classify_triangle(1,1,2**.5))
    print("Sides: 3,4,5 is " + classify_triangle(3,4,5))
    

main()
my_brand("SSW 567 HW 01 Testing Triangle Classificaiton")  