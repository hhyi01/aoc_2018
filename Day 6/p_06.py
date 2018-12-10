
#p6
import sys

with open('/Users/hyi/Desktop/aoc_2018/Day 6/p_06_input.txt') as f:
    p6_input = f.readlines()

p6_input = [(x.strip().split(', ')) for x in p6_input]

sample_input = [['1', '1'], ['1', '6'], ['8', '3'], ['3', '4'], ['5', '5'], ['8', '9']]

def get_extreme_top(set_of_coordinates):
    min_y = sys.maxint
    for coordinate in set_of_coordinates:
        if int(coordinate[1]) < min_y:
            min_y = int(coordinate[1])
    return min_y

def get_extreme_left(set_of_coordinates):
    min_x = sys.maxint
    for coordinate in set_of_coordinates:
        if int(coordinate[0]) < min_x:
            min_x = int(coordinate[0])
    return min_x

def get_extreme_bottom(set_of_coordinates):
    max_y = -sys.maxint - 1
    for coordinate in set_of_coordinates:
        if int(coordinate[1]) > max_y:
            max_y = int(coordinate[1])
    return max_y

def get_extreme_right(set_of_coordinates):
    max_x = -sys.maxint - 1
    for coordinate in set_of_coordinates:
        if int(coordinate[0]) > max_x:
            max_x = int(coordinate[0])
    return max_x

def calculate_manhattan_distance(coordinate1, coordinate2):
    x_distance = abs(int(coordinate1[0]) - int(coordinate2[0]))
    y_distance = abs(int(coordinate1[1]) - int(coordinate2[1]))
    manhattan_distance = x_distance + y_distance
    return manhattan_distance

def calculate_areas_of_coordinates(top, left, bottom, right, set_of_coordinates):
    coordinates_areas = {}
    for coordinate in set_of_coordinates:
        for x in range(left, right):
            for y in range(top, bottom):
                key = str(str(x) + ', ' + str(y))
                if key not in coordinates_areas:
                    coordinates_areas[key] = {}
                string_coordinate = str(str(coordinate[0]) + ', ' + str(coordinate[1]))
                coordinates_areas[key][string_coordinate] = calculate_manhattan_distance([x, y], coordinate)
    return coordinates_areas

def get_minimum_distances(areas_of_coordinates):
    min_distances = {}
    for area in areas_of_coordinates:
        min_distance = get_min_distance(areas_of_coordinates[area])
        min_distances[area] = get_min_distance_keys(areas_of_coordinates[area], min_distance)
    return min_distances

def get_min_distance(set_of_distances):
    min_distance = sys.maxint
    for distance in set_of_distances:
        if set_of_distances[distance] < min_distance:
            min_distance = set_of_distances[distance]
    return min_distance

def get_min_distance_keys(set_of_distances, search_value):
    distance_keys = []
    for distance in set_of_distances:
        if set_of_distances[distance] == search_value:
            distance_keys.append(distance)
    return distance_keys

def get_count_of_closest(set_of_coordinates, min_distance_keys):
    count_of_closest = {}
    for coordinate in set_of_coordinates:
        coord = str(str(coordinate[0]) + ', ' + str(coordinate[1]))
        if coord not in count_of_closest:
            count_of_closest[coord] = 0
        for key in min_distance_keys:
            if len(min_distance_keys[key]) == 1:
                if coord in min_distance_keys[key]:
                    count_of_closest[coord] += 1
    return count_of_closest

def get_largest_area(count_of_closest_coordinates):
    max_area_key = max(count_of_closest_coordinates, key=count_of_closest_coordinates.get)
    return count_of_closest_coordinates[max_area_key]

#p2
def get_total_distances(top, left, bottom, right, set_of_coordinates):
    coordinates_total_distances = {}
    for coordinate in set_of_coordinates:
        for x in range(left, right):
            for y in range(top, bottom):
                key = str(str(x) + ', ' + str(y))
                if key not in coordinates_total_distances:
                    coordinates_total_distances[key] = 0
                coordinates_total_distances[key] += calculate_manhattan_distance([x, y], coordinate)
    return coordinates_total_distances

def distances_within_region(total_distances, distance_to_all=32):
    within_region = {}
    for coordinate in total_distances:
        if total_distances[coordinate] < distance_to_all:
            within_region[coordinate] = total_distances[coordinate]
    return within_region

#p1 and p2
top = get_extreme_top(p6_input)
left = get_extreme_left(p6_input)
bottom = get_extreme_bottom(p6_input)
right = get_extreme_right(p6_input)

#p1
coordinate_areas = calculate_areas_of_coordinates(top, left, bottom, right, p6_input)
minimum_distances = get_minimum_distances(coordinate_areas)
closest_coordinates_counts = get_count_of_closest(p6_input, minimum_distances)
largest_area = get_largest_area(closest_coordinates_counts)

#p2
total_distances = get_total_distances(top, left, bottom, right, p6_input)
region_coordinates = distances_within_region(total_distances, 10000)
region_size = len(region_coordinates)
