#adventofcode
with open('p_01.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

#p1, part 1
class FreqManager():
  def __init__(self):
    self.freq_counter = {}

  def freq_calculator(self, freq_list):
    final_result = 0
    for freq in freq_list:
      final_result = final_result + int(freq)
    return final_result

  #p1, part 2
  def dupe_freq(self, freq_list):
    final_result = 0
    while 2 not in self.freq_counter.values():
      for freq in freq_list:
        final_result = final_result + int(freq)
        if final_result not in self.freq_counter:
          self.freq_counter[final_result] = 1
        else: 
          return final_result
          break