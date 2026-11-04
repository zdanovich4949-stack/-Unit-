import unittest
import circle
import rectangle
import square
import triangle

class RectlangleTestCase(unittest.TestCase):
    def test_area(self):
        res = rectangle.area(8,4)
        self.assertEqual(res, 32)
    def test_perimeter(self):
        res = rectangle.perimeter(8,4)
        self.assertEqual(res, 24)

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        res = circle.area(5)
        self.assertEqual(res, 78.53981633974483)
    def test_perimeter(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 31.41592653589793)

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        res = square.area(228)
        self.assertEqual(res, 51984)
    def test_perimeter(self):
        res = square.perimeter(228)
        self.assertEqual(res, 912)

class TriangletestCase(unittest.TestCase):
    def test_area(self):
        res = triangle.area(2,8)
        self.assertEqual(res, 8.0)
    def test_perimeter(self):
        res = triangle.perimeter(2, 777, 322)
        self.assertEqual(res, 1101)