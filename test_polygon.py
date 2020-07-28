from math import isclose
from polygon import Polygon
import unittest


class TestPolygon(unittest.TestCase):
    rel_tol = 0.001
    abs_tol = 0.001

    def setUp(self):
        self.p = Polygon(3, 1)
        self.p2 = Polygon(3, 1)
        self.p3 = Polygon(5, 2)

    def test_data_validations(self):
        with self.assertRaises(TypeError):
            p_ = Polygon('3', 1)
        with self.assertRaises(TypeError):
            p_ = Polygon(3, '1')
        with self.assertRaises(ValueError):
            p_ = Polygon(1, 3)

    def test_repr(self):
        self.assertEqual(str(self.p), 'Polygon(n=3, R=1)')

    def test_eq(self):
        self.assertTrue(self.p == self.p2)
        self.assertFalse(self.p == self.p3)

    def test_gt(self):
        self.assertTrue(self.p3 > self.p)
        self.assertFalse(self.p2 > self.p3)

    def test_edge(self):
        self.assertEqual(self.p.edges, 3)
        self.assertEqual(self.p3.edges, 5)

    def test_vertices(self):
        self.assertEqual(self.p.vertices, 3)
        self.assertEqual(self.p3.vertices, 5)

    def test_circumradius(self):
        self.assertEqual(self.p.circumradius, 1)
        self.assertEqual(self.p3.circumradius, 2)

    def test_interior_angle(self):
        self.assertEqual(self.p.interior_angle, 60)
        self.assertEqual(self.p3.interior_angle, 108)
        with self.assertRaises(AttributeError):
            self.p.interior_angle = 999

    def test_edge_length(self):
        self.assertTrue(isclose(self.p.edge_length, 1.73205,
                                rel_tol=TestPolygon.rel_tol,
                                abs_tol=TestPolygon.abs_tol))
        self.assertTrue(isclose(self.p3.edge_length, 2.35114,
                                rel_tol=TestPolygon.rel_tol,
                                abs_tol=TestPolygon.abs_tol))
        with self.assertRaises(AttributeError):
            self.p.edge_length = 888

    def test_apothem(self):
        self.assertTrue(isclose(self.p.apothem, 0.5,
                                rel_tol=TestPolygon.rel_tol,
                                abs_tol=TestPolygon.abs_tol))
        self.assertTrue(isclose(self.p3.apothem, 1.61803,
                                rel_tol=TestPolygon.rel_tol,
                                abs_tol=TestPolygon.abs_tol))
        with self.assertRaises(AttributeError):
            self.p.apothem = 777

    def test_area(self):
        self.assertTrue(isclose(self.p.area, 1.29904,
                                rel_tol=TestPolygon.rel_tol,
                                abs_tol=TestPolygon.abs_tol))
        self.assertTrue(isclose(self.p3.area, 9.51057,
                                rel_tol=TestPolygon.rel_tol,
                                abs_tol=TestPolygon.abs_tol))
        with self.assertRaises(AttributeError):
            self.p.area = 666

    def test_perimeter(self):
        self.assertTrue(isclose(self.p.perimeter, 5.19615,
                                rel_tol=TestPolygon.rel_tol,
                                abs_tol=TestPolygon.abs_tol))
        self.assertTrue(isclose(self.p3.perimeter, 11.7557,
                                rel_tol=TestPolygon.rel_tol,
                                abs_tol=TestPolygon.abs_tol))
        with self.assertRaises(AttributeError):
            self.p.area = 555


if __name__ == '__main__':
    unittest.main()
