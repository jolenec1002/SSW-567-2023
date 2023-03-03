import unittest
import math

from triangle_classifying import classify_triangle

from mybrand import my_brand
my_brand("SSW 567 HW 05-Static Code Analysis")

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testScaRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Scalene and Right')

    def testScaRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,12,13),'Scalene and Right')
        
    def testEqualTriangleA(self): 
        self.assertEqual(classify_triangle(6,6,6),'Equilateral')

    def testEqualTriangleB(self): 
        self.assertEqual(classify_triangle(56,56,56),'Equilateral')
    
    def testEqualTriangleC(self): 
        self.assertEqual(classify_triangle(5.3,5.3,5.3),'Equilateral')

    def testIsoTriangleA(self): 
        self.assertEqual(classify_triangle(4,4,6),'Isosceles')

    def testIsoTriangleB(self): 
        self.assertEqual(classify_triangle(46,46,25),'Isosceles')

    def testIsoTriangleC(self): 
        self.assertEqual(classify_triangle(1.23,1.23,2),'Isosceles')

    def testIsoRightA(self): 
        self.assertEqual(classify_triangle(2,2,math.sqrt(8)),'Isosceles and Right')

    def testIsoRightB(self): 
        self.assertEqual(classify_triangle(3,3,math.sqrt(18)),'Isosceles and Right')

    def testScaTriangleA(self): 
        self.assertEqual(classify_triangle(7,10,14),'Scalene')

    def testScaTriangleB(self): 
        self.assertEqual(classify_triangle(15,13,20),'Scalene')

    def testScaTriangleC(self): 
        self.assertEqual(classify_triangle(3.56, 7.2, 4),'Scalene')

    def testZeroInputA(self): 
        self.assertEqual(classify_triangle(0,1,2),'InvalidInput')

    def testZeroInputB(self): 
        self.assertEqual(classify_triangle(1,0,2),'InvalidInput')

    def testZeroInputC(self): 
        self.assertEqual(classify_triangle(2,1,0),'InvalidInput')

    def testLargeInputA(self): 
        self.assertEqual(classify_triangle(201,100,150),'InvalidInput')

    def testLargeInputB(self): 
        self.assertEqual(classify_triangle(100,201,150),'InvalidInput')

    def testLargeInputC(self): 
        self.assertEqual(classify_triangle(100,150,201),'InvalidInput')

    def testNotTriangleA(self): 
        self.assertEqual(classify_triangle(1,1,2),'NotATriangle')

    def testNotTriangleB(self): 
        self.assertEqual(classify_triangle(5,6,13),'NotATriangle')

    def testOrderA(self): 
        self.assertEqual(classify_triangle(5,4,3),'Scalene and Right')

    def testOrderB(self): 
        self.assertEqual(classify_triangle(12,13,5),'Scalene and Right')

    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

