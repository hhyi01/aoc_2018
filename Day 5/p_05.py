#p5
import sys

sample_input = 'dabAcCaCBAcCcaDA' #result = 'dabCBAcaDA'

letters = 'abcdefghijklmnopqrstuvwxyz'

with open('/Users/hyi/Desktop/aoc_2018/Day 5/p_05_input.txt') as f:
    p5_input = f.readlines()

p5_input = p5_input[0]

def remove_reacting_units(polymer):
  i = 0
  while i < len(polymer) - 1:
    index = 0
    if polymer[i].lower() == polymer[i + 1].lower():
      if (polymer[i].islower() and polymer[i + 1].isupper()) or (polymer[i].isupper() and polymer[i + 1].islower()):
        polymer = polymer[:i] + polymer[(i+2):]
        index = i-1
    if index != 0:
      i = index
    else:
      i += 1
  return polymer

# print remove_reacting_units(sample_input)
# remaining_units = remove_reacting_units(p5_input)
# print len(remaining_units)

def remove_unit(unit_to_remove, polymer):
  i = 0
  while i < len(polymer) - 1:
    index = 0
    if polymer[i].lower() == unit_to_remove.lower():
      polymer = polymer[:i] + polymer[(i+1):]
      index = i
    if index != 0:
      i = index
    else:
      i += 1
  return polymer

def collapse_counts(polymer):
  collapsed_polymers = {}
  for letter in letters:
    if letter in polymer.lower():
      polymer_unit_removed = remove_unit(letter, polymer)
      reacted_polymer = remove_reacting_units(polymer_unit_removed)
      collapsed_polymers[letter] = len(reacted_polymer)
  return collapsed_polymers
  
def get_shortest_polymer(polymer_collapse_counts):
  shortest_polymer = sys.maxint
  for polymer in polymer_collapse_counts:
    if polymer_collapse_counts[polymer] < shortest_polymer:
      shortest_polymer = polymer_collapse_counts[polymer]
  return shortest_polymer

polymer_variations = collapse_counts(p5_input)
print get_shortest_polymer(polymer_variations)
