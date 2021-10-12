import math
from random import randint


def getPoints():
    points = []
    # get input
    num_points = input('Choose how many points you would like to use: (2 or more) ')
    while int(num_points) < 2:
        num_points = input('Invalid input, choose how many points you would like to use: (2 or more) ')
    # create random points based on the user input from 1 to 10,000
    for i in range(int(num_points)):
        x = randint(1, 10000)
        y = randint(1, 10000)
        points.append([x, y])
    return points


# given 2 points calculate the distance
def calculate_distance(p_1, p_2):
    # distance = sqrt((x2 - x1)^2 + (y2 -y1)^2)
    d = math.sqrt(math.pow(float(p_2[0]) - float(p_1[0]), 2) +
                  math.pow(float(p_2[1]) - float(p_1[1]), 2))
    return d


def create_list_of_distances(points):
    p_info = []
    # iterate all points and calculate the distance bw all other points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = calculate_distance(points[i], points[j])
            p_info.append({'x1': points[i][0], 'y1': points[i][1], 'x2': points[j][0], 'y2': points[j][1], 'distance': distance})
    return p_info


def merge_sort(p):

    list_length = len(p)

    # base case
    if list_length == 1:
        return p

    # Get the middle of the list
    # // = integer division
    mid_point = list_length // 2

    # recursively merge everythin in the left and everything in the right
    left_partition = merge_sort(p[:mid_point])
    right_partition = merge_sort(p[mid_point:])

    # merge everything back into one
    return merge(left_partition, right_partition)


# takes in two lists and returns a sorted list made up of the content within the two lists
def merge(left, right):
    output = []
    i = j = 0

    # Executes the while loop if both pointers i and j are less than the length of the left and right lists
    while i < len(left) and j < len(right):
        # Compare the elements at every position of both lists during each iteration

        if left[int(i)]['distance'] < right[int(j)]['distance']:
            # output is populated with the lesser value
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    # The remnant elements are picked from the current pointer value to the end of the respective list
    output.extend(left[i:])
    output.extend(right[j:])

    return output


if __name__ == '__main__':
    count = 0
    all_points = getPoints()
    points_info = create_list_of_distances(all_points)
    m = input('How many closest pairs?: ')
    while int(m) >= len(all_points):
        m = input('Not enough points to calculate that many closest pairs, choose less closest pairs?: ')
    sorted_points_info = merge_sort(points_info)
    for i in range(int(m)):
        print(sorted_points_info[i])

