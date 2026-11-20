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
    def test_negative_area(self):
        res = rectangle.area(-4,4)
        self.assertEqual(res, 0)
    def test_negative_perimeter(self):
        res = rectangle.perimeter(-4,3)
        self.assertEqual(res, 0)
    def test_string_area(self):
        with self.assertRaises(ValueError):
            rectangle.area("sdfghjk","lkjhg")
    def test_string_perimeter(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter("sdfghjk","zxcvbn")


class CircleTestCase(unittest.TestCase):
    def test_area(self):
        res = circle.area(5)
        self.assertEqual(res, 78.53981633974483)

    def test_perimeter(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 31.41592653589793)

    def test_negative_area(self):
        res = circle.area(-4)
        self.assertEqual(res, 0)

    def test_negative_perimeter(self):
        res = circle.perimeter(-4)
        self.assertEqual(res, 0)

    def test_string_area(self):
        with self.assertRaises(ValueError):
            circle.area("sdfghjk")
    def test_string_perimeter(self):
        with self.assertRaises(ValueError):
            circle.perimeter("sdfghjk")

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        res = square.area(228)
        self.assertEqual(res, 51984)
    def test_perimeter(self):
        res = square.perimeter(228)
        self.assertEqual(res, 912)
    def test_negative_area(self):
        res = square.area(-4)
        self.assertEqual(res, 0)
    def test_negative_perimeter(self):
        res = square.perimeter(-4)
        self.assertEqual(res, 0)
    def test_string_area(self):
        with self.assertRaises(ValueError):
            square.area("sdfghjk")
    def test_string_perimeter(self):
        with self.assertRaises(ValueError):
            square.perimeter("sdfghjk")

class TriangletestCase(unittest.TestCase):
    def test_area(self):
        res = triangle.area(2,8)
        self.assertEqual(res, 8.0)
    def test_perimeter(self):
        res = triangle.perimeter(2, 777, 322)
        self.assertEqual(res, 1101)
    def test_negative_area(self):
        res = triangle.area(-4,4)
        self.assertEqual(res, 0)
    def test_negative_perimeter(self):
        res = triangle.perimeter(-4,4,2)
        self.assertEqual(res, 0)
    def test_string_area(self):
        with self.assertRaises(ValueError):
            triangle.area("sdfghjk","werty")
    def test_string_perimeter(self):
        with self.assertRaises(ValueError):
            triangle.perimeter("sdfghjk","werty", "poiuy")