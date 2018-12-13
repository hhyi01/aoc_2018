#Day 3
import sys

sample_input = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']

#n of nxn dimension of fabric square
n = 1000

with open('/Users/hyi/Desktop/aoc_2018/Day 3/p_03_input.txt') as f:
    p_03_input = f.readlines()

p_03_input = [x.strip() for x in p_03_input]

def parse_input(input_list): 
    parsed_input = {}
    for item in input_list:
        item_id = item.split(' @ ')[0]
        details = [item.split('@ ')[1].split(':')[0], item.split('@ ')[1].split(': ')[1]]
        parsed_input[item_id] = details
    return parsed_input

def calculate_squares(parsed_input, n):
    all_squares = {}
    for item in parsed_input:
        all_squares[item] = {}
        x_left = int(parsed_input[item][0].split(',')[0])
        x_right = int(x_left) + int(parsed_input[item][1].split('x')[0])
        y_top = n - int(parsed_input[item][0].split(',')[1])
        y_bottom = int(y_top) - int(parsed_input[item][1].split('x')[1])
        all_squares[item]['x_left'] = x_left
        all_squares[item]['x_right'] = x_right
        all_squares[item]['y_top'] = y_top
        all_squares[item]['y_bottom'] = y_bottom
    return all_squares

def assign_fabric_ids_to_coordinate(all_squares):
    fabric_coordinates = {}
    for sq in squares:
        square = squares[sq]
        for x in range(square['x_left'], square['x_right']):
            for y in range(square['y_bottom'], square['y_top']):
                coordinate = str(x) + ',' + str(y)
                if coordinate not in fabric_coordinates:
                    fabric_coordinates[coordinate] = 1
                else:
                    fabric_coordinates[coordinate] += 1
    return fabric_coordinates

def square_inches_in_two_plus_claims(fabric_coordinates, claims):
    inches = 0
    for inch in fabric_coordinates:
        if fabric_coordinates[inch] >= claims:
            inches += 1
    return inches

def get_non_overlapping_claim(fabric_coordinates, squares):
    square_id = ''
    square_inches = 0
    overlap_count = 0
    for sq in squares:
        square = squares[sq]
        for x in range(square['x_left'], square['x_right']):
            for y in range(square['y_bottom'], square['y_top']):
                coordinate = str(x) + ',' + str(y)
                square_inches += 1
                overlap_count += fabric_coordinates[coordinate]
        if square_inches == overlap_count:
            square_id = sq
        else:
            square_inches = 0
            overlap_count = 0
    return square_id

#p1
sample_input = parse_input(sample_input)
p_03_input = parse_input(p_03_input)
squares = calculate_squares(p_03_input, n)
fabric_coordinates = assign_fabric_ids_to_coordinate(squares)
inches_2_or_more_claims = square_inches_in_two_plus_claims(fabric_coordinates, 2)

#p2
print get_non_overlapping_claim(fabric_coordinates, squares)




