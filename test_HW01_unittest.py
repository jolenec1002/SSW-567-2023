import unittest
import HW01

class Test(unittest.TestCase):
    
    # Equilateral Test
    def test01(self):
        self.assertEqual(HW01.classify_triangle(1,1,1), "Equilateral")
        self.assertEqual(HW01.classify_triangle(100,100,100), "Equilateral")
        self.assertEqual(HW01.classify_triangle(.5,.5,.5), "Equilateral")

    # Isosceles Test
    def test02(self):
        self.assertEqual(HW01.classify_triangle(3,5,5), "Isosceles")
        self.assertEqual(HW01.classify_triangle(5,5,3), "Isosceles")
        self.assertEqual(HW01.classify_triangle(.2,.2,6), "Isosceles")

    # Scalene Test
    def test03(self):
        self.assertEqual(HW01.classify_triangle(3,6,7), "Scalene")
        self.assertEqual(HW01.classify_triangle(.1,.2,.3), "Scalene")
        self.assertEqual(HW01.classify_triangle(50,43,78), "Scalene")

     # Isosceles and Right Test
    def test04(self):
        self.assertEqual(HW01.classify_triangle(1,1,2**.5), "Isosceles and Right")
        self.assertEqual(HW01.classify_triangle(2,2,8**.5), "Isosceles and Right")
        self.assertEqual(HW01.classify_triangle(5,5,50**.5), "Isosceles and Right")

    # Scalene and Right Test
    def test05(self):
        self.assertEqual(HW01.classify_triangle(3,4,5), "Scalene and Right")
        self.assertEqual(HW01.classify_triangle(5,12,13), "Scalene and Right")
        self.assertEqual(HW01.classify_triangle(21,28,35), "Scalene and Right")

    # Not a Triangle Test
    def test05(self):
        self.assertEqual(HW01.classify_triangle(3,4,0), "Not a triangle")
        self.assertEqual(HW01.classify_triangle(3,0,1), "Not a triangle")
        self.assertEqual(HW01.classify_triangle(0,4,2), "Not a triangle")
        
    



      


if __name__ == "__main__":
    unittest.main()