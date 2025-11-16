import unittest
import math
from circle import Circle

class test_circle(unittest.TestCase):
    
    def test_getRadius_pos(self):
        c = Circle(10)
        self.assertEqual(c.getRadius(), 10)

        c2 = Circle(200)
        self.assertEqual(c2.getRadius(), 200)

        c3 = Circle(3000)
        self.assertEqual(c3.getRadius(), 3000)

    def test_getRadius_neg(self):
        c = Circle(-10)
        self.assertEqual(c.getRadius(), -10)

        c2 = Circle(-200)
        self.assertEqual(c2.getRadius(), -200)

        c3 = Circle(-3000)
        self.assertEqual(c3.getRadius(), -3000)

    def test_getRadius_dec(self):
        c = Circle(10.21)
        self.assertEqual(c.getRadius(), 10.21)

        c2 = Circle(200.47)
        self.assertEqual(c2.getRadius(), 200.47)

        c3 = Circle(3000.39)
        self.assertEqual(c3.getRadius(), 3000.39)

    def test_setRadius_pos(self):
        c = Circle(10)
        self.assertEqual(c.setRadius(20), True)

        c2 = Circle(200)
        self.assertEqual(c2.setRadius(400), True)

        c3 = Circle(3000)
        self.assertEqual(c3.setRadius(6000), True)

    def test_setRadius_neg(self):
        c = Circle(10)
        self.assertEqual(c.setRadius(-20), False)

        c2 = Circle(200)
        self.assertEqual(c2.setRadius(-400), False)

        c3 = Circle(3000)
        self.assertEqual(c3.setRadius(-6000), False)

    def test_setRadius_dec_pos(self):
        c = Circle(10)
        self.assertEqual(c.setRadius(20.10), True)

        c2 = Circle(200)
        self.assertEqual(c2.setRadius(400.20), True)

        c3 = Circle(3000)
        self.assertEqual(c3.setRadius(6000.30), True)

    def test_setRadius_dec_neg(self):
        c = Circle(10)
        self.assertEqual(c.setRadius(-20.10), False)

        c2 = Circle(200)
        self.assertEqual(c2.setRadius(-400.20), False)

        c3 = Circle(3000)
        self.assertEqual(c3.setRadius(-6000.30), False)

    def test_getArea_pos(self):
        c = Circle(10)
        expected = math.pi * 10 * 10
        self.assertEqual(c.getArea(), expected)

        c2 = Circle(200)
        expected = math.pi * 200 * 200
        self.assertEqual(c2.getArea(), expected)

        c3 = Circle(3000)
        expected = math.pi * 3000 * 3000
        self.assertEqual(c3.getArea(), expected)

    def test_getArea_pos2(self):
        c = Circle(10)
        expected = math.pi * 10 * 10
        self.assertAlmostEqual(c.getArea(), expected, places = 3)

        c2 = Circle(200)
        expected = math.pi * 200 * 200
        self.assertAlmostEqual(c2.getArea(), expected, places = 3)

        c3 = Circle(3000)
        expected = math.pi * 3000 * 3000
        self.assertAlmostEqual(c3.getArea(), expected, places = 3)

    def test_getArea_neg(self):
        c = Circle(-10)
        expected = math.pi * -10 * -10
        self.assertEqual(c.getArea(), expected)

        c2 = Circle(-200)
        expected = math.pi * -200 * -200
        self.assertEqual(c2.getArea(), expected)

        c3 = Circle(-3000)
        expected = math.pi * -3000 * -3000
        self.assertEqual(c3.getArea(), expected)

    def test_getArea_neg2(self):
        c = Circle(-10)
        expected = math.pi * -10 * -10
        self.assertAlmostEqual(c.getArea(), expected, places = 3)

        c2 = Circle(-200)
        expected = math.pi * -200 * -200
        self.assertAlmostEqual(c2.getArea(), expected, places = 3)

        c3 = Circle(-3000)
        expected = math.pi * -3000 * -3000
        self.assertAlmostEqual(c3.getArea(), expected, places = 3)

    def test_getArea_checker(self):
        c = Circle(2)
        self.assertEqual(c.getArea(), 0)

        c2 = Circle(10)
        c2.setRadius(2)
        self.assertEqual(c2.getArea(), 0)

if __name__ == "__main__":
    unittest.main()