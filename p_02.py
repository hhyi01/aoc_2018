#p2
p2_sample_input = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']

#load input
with open('p_02.txt') as f:
    p2 = f.readlines()

p2 = [x.strip() for x in p2]

def get_checksum(id_list):
  id_letter_counts = {}
  ids_with_2_dupes = []
  ids_with_3_dupes = []
  for i in id_list:
    id_letter_counts[i] = get_letter_count(i)
  for an_id in id_letter_counts:
    if 2 in id_letter_counts[an_id].values():
      ids_with_2_dupes.append(an_id)
    if 3 in id_letter_counts[an_id].values():
      ids_with_3_dupes.append(an_id)
  return len(ids_with_2_dupes) * len(ids_with_3_dupes) #checksum
  # return id_letter_counts

def get_letter_count(some_id):
  id_count = {}
  for letter in some_id:
    if letter not in id_count:
      id_count[letter] = 1
    else: 
      id_count[letter] += 1
  return id_count

# print 'sample checksum', get_checksum(p2_sample_input) #12
# print 'input checksum', get_checksum(p2) #7470

sample_ids = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

def string_comparison(word1, word2):
  overlap_count = {}
  counter = 0
  key = ''
  for i in range(0, len(word1)):
    if word1[i] == word2[i]:
      key = key + word1[i]
      counter += 1
  if counter == (len(word1) - 1):
    overlap_count[key] = counter
  return overlap_count

def get_overlap(a_list):
  overlap_ids = {}
  for a_word in a_list:
    for b_word in a_list:
      if a_word != b_word:
        overlap_ids.update(string_comparison(a_word, b_word))
  return overlap_ids

# print get_overlap(sample_ids) #fgij
# print get_overlap(p2) #kqzxdenujwcstybmgvyiofrrd