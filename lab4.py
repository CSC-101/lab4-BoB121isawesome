import data
import math

# Write your functions for each part in the space below.

# Part 1
def first_element(first:list[list[int]]):
    first_list=[]
    for sublist in first:
        if len(sublist)>0:
            first_list.append(sublist[0])
    return first_list

# Part 2
def x_coordinates(point):
    first_x = []
    for t in point:
        first_x.append(t.x)
    return first_x

# Part 3
def are_in_positive_quadrant(points):
    points_list = []
    for point in points:
        if point.x>0 and point.y>0:
            points_list.append((point.x,point.y))
    return points_list

# Part 4
def distance(point1, point2):
    return math.sqrt((point1.x-point2.x)**2+(point1.y-point2.y)**2)

# Part 5
def manhattan_distance(point1, point2):
    return float(abs(point1.x-point2.x)+abs(point1.y-point2.y))

# Part 6
def distance_all(points):
    output_list = []
    for point in points:
        output_list.append(math.sqrt((point.x-0)**2+(point.y-0)**2))
    return output_list
