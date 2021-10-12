import unittest
import main


class TestStringMethods(unittest.TestCase):

    def test_distance_calculation(self):
        distance = main.calculate_distance([2, 2], [3, 2])
        self.assertEqual(distance, 1)
        distance = main.calculate_distance([3, 2], [7, 2])
        self.assertEqual(distance, 4)

    def test_create_list_of_distances(self):
        points = [[2, 2], [3, 2], [7, 2]]
        augmented_points = main.create_list_of_distances(points)
        self.assertEqual(augmented_points, [{'x1': 2, 'y1': 2, 'x2': 3, 'y2': 2,
                                             'distance': 1.0}, {'x1': 2, 'y1': 2, 'x2': 7, 'y2': 2,
                                                                'distance': 5.0}, {'x1': 3, 'y1': 2, 'x2': 7,
                                                                                   'y2': 2, 'distance': 4.0}])

    def test_merge_order(self):
        unordered_list = [{'x1': 2, 'y1': 2, 'x2': 3, 'y2': 2, 'distance': 1.0},
                          {'x1': 2, 'y1': 2, 'x2': 7, 'y2': 2, 'distance': 5.0},
                          {'x1': 3, 'y1': 2, 'x2': 7, 'y2': 2, 'distance': 4.0}]
        sorted_list = main.merge_sort(unordered_list)
        # convert the list of points dicts to a list of distances only
        distances = []
        for i in sorted_list:
            distances.append(i['distance'])
        # confirm the distances are in order
        self.assertEqual(distances, [1, 4, 5])

        ordered_list = [{'x1': 2, 'y1': 2, 'x2': 3, 'y2': 2, 'distance': 1.0},
                        {'x1': 3, 'y1': 2, 'x2': 7, 'y2': 2, 'distance': 4.0},
                        {'x1': 2, 'y1': 2, 'x2': 7, 'y2': 2, 'distance': 5.0}]
        sorted_list = main.merge_sort(ordered_list)
        # convert the list of points dicts to a list of distances only
        distances = []
        for i in sorted_list:
            distances.append(i['distance'])
        # confirm the distances are in order
        self.assertEqual(distances, [1, 4, 5])


if __name__ == '__main__':
    unittest.main()