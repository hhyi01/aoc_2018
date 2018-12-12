#p1
import sys

p_11_input = 1309

#rack ID = x-coordinate + 10
#intial power level = rack ID * y-coordinate
#increase power level by grid serial number (input)
#set power level to itself * rack ID
#keep on hundreds digit of power level
#subtract 5 from power level

def get_power_level(coordinate, grid_serial_number):
    rack_id = coordinate[0] + 10
    init_power_level = rack_id * coordinate[1]
    power_level = init_power_level + grid_serial_number
    power_level = power_level * rack_id
    hundreds_digits = str(power_level)[:-2]
    hundreds_digits = hundreds_digits[-1:]
    return int(hundreds_digits) - 5

# print get_power_level([3,5], 8) #example => 4
# print get_power_level([122,79], 57) #122,79 => -5
# print get_power_level([217,196], 39) #217,196 => 0
# print get_power_level([101,153], 71) #101,153 => 4

def calculate_power_levels(grid_size, grid_serial_number):
    power_levels = {}
    for x in range(1, grid_size + 1):
        for y in range(1, grid_size + 1):
            coordinate = [ x, y ]
            power_level = get_power_level(coordinate, grid_serial_number)
            key = str(x) + ',' + str(y)
            power_levels[key] = power_level
    return power_levels

def calculate_sub_grid(sub_grid_size, power_levels, coordinate, grid_size):
    total_power_level = 0
    if coordinate[0] + sub_grid_size <= grid_size:
        if coordinate[1] + sub_grid_size <= grid_size:
            for x in range(coordinate[0], coordinate[0] + sub_grid_size):
                for y in range(coordinate[1], coordinate[1] + sub_grid_size):
                    # modified for part 2
                    key = str(x) + ',' + str(y)
                    total_power_level += power_levels[key]
    return total_power_level

def get_power_levels_all_sub_grids(grid_size, power_levels, sub_grid_size):
    sub_grid_power_levels = {}
    for x in range(1, grid_size + 1):
        for y in range(1, grid_size + 1):
            coordinate = [ x, y ]
            sub_grid = calculate_sub_grid(sub_grid_size, power_levels, coordinate, grid_size)
            key = str(x) + ',' + str(y) + ',' + str(sub_grid_size) 
            sub_grid_power_levels[key] = sub_grid
    return sub_grid_power_levels

def get_max_sub_grid(sub_grids):
    max_sub_grid = -sys.maxint
    max_sub_id = ''
    for grid in sub_grids:
        if sub_grids[grid] > max_sub_grid:
            max_sub_grid = sub_grids[grid]
            max_sub_id = grid
    return [max_sub_id, max_sub_grid]

#p1
# power_levels = calculate_power_levels(300, grid_serial_number=p_11_input)
# sub_grids = get_power_levels_all_sub_grids(300, power_levels, 3)
# max_sub_grid = get_max_sub_grid(sub_grids)

#p2
power_levels = calculate_power_levels(300, grid_serial_number=p_11_input)
sub_grid = get_power_levels_all_sub_grids(300, power_levels, 12)
all_max_sub_grids = {}

# this output hits a peak at 233,271,13 and steadily falls until max power levels become negative 
# around iteration 50
for i in range(1, 20):
    sub_grid_levels = get_power_levels_all_sub_grids(300, power_levels, i)
    max_sub_grid = get_max_sub_grid(sub_grid_levels)
    key = max_sub_grid[0]
    val = max_sub_grid[1]
    all_max_sub_grids[key] = val
    print i, key, val



