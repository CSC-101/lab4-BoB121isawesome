
import lab4
import unittest
from data import Point

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1, 2], [3, 4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)

    def test_first_element_2(self):
        input = [[5, 2, 2], [], [3, 4]]
        result = lab4.first_element(input)
        expected = [5, 3]
        self.assertEqual(expected, result)


    # Part 2
    def test_x_coordinates_1(self):
        point1 = Point(1,2)
        point2 = Point(5,4)
        point3 = Point(1,2)
        points_list = [point1, point2, point3]
        result = lab4.x_coordinates(points_list)
        expected = [1,5,1]
        self.assertEqual(expected, result)

    def test_x_coordinates_2(self):
        point4 = Point(42,2)
        point5 = Point(15,4)
        point6 = Point(23,2)
        points_list = [point4, point5, point6]
        result = lab4.x_coordinates(points_list)
        expected = [42,15,23]
        self.assertEqual(expected, result)


    # Part 3
    def test_are_in_positive_quadrant_1(self):
        point4 = Point(42, -2)
        point5 = Point(-15, 4)
        point6 = Point(23, 2)
        points_list = [point4, point5, point6]
        result = lab4.are_in_positive_quadrant(points_list)
        expected = [(23,2)]
        self.assertEqual(expected, result)

    def test_are_in_positive_quadrant_2(self):
        point4 = Point(42, 23)
        point5 = Point(15, -34)
        point6 = Point(3, 25)
        points_list = [point4, point5, point6]
        result = lab4.are_in_positive_quadrant(points_list)
        expected = [(42,23),(3,25)]
        self.assertEqual(expected, result)


    # Part 4
    def test_distance_1(self):
        point1 = Point(2, 3)
        point2 = Point(-4, -5)
        result = lab4.distance(point1, point2)
        expected = 10
        self.assertEqual(expected, result)

    def test_distance_2(self):
        point1 = Point(-2, -14)
        point2 = Point(10, 21)
        result = lab4.distance(point1, point2)
        expected = 37
        self.assertEqual(expected, result)


    # Part 5
    def test_manhattan_distance_1(self):
        point1 = Point(-2, -13)
        point2 = Point(10, 21)
        result = lab4.manhattan_distance(point1, point2)
        expected = 46
        self.assertEqual(expected, result)

    def test_manhattan_distance_2(self):
        point1 = Point(5, 34)
        point2 = Point(-5, 1)
        result = lab4.manhattan_distance(point1, point2)
        expected = 43
        self.assertEqual(expected, result)


    # Part 6
    def test_distance_all_1(self):
        point1 = Point(3, 4)
        point2 = Point(8, 6)
        points_list = [point1, point2]
        result = lab4.distance_all(points_list)
        expected = [5,10]
        self.assertEqual(expected, result)

    def test_distance_all_2(self):
        point1 = Point(5, -12)
        point2 = Point(-16, 63)
        points_list = [point1, point2]
        result = lab4.distance_all(points_list)
        expected = [13,65]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()