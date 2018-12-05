#p4
from collections import OrderedDict
from datetime import datetime

with open('p_04.txt') as f:
    schedule = f.readlines()

schedule = [x.strip() for x in schedule]

sample_schedule = ['[1518-11-01 00:00] Guard #10 begins shift', '[1518-11-01 00:05] falls asleep', 
'[1518-11-01 00:25] wakes up',
'[1518-11-01 00:30] falls asleep',
'[1518-11-01 00:55] wakes up',
'[1518-11-01 23:58] Guard #99 begins shift',
'[1518-11-02 00:40] falls asleep',
'[1518-11-02 00:50] wakes up',
'[1518-11-03 00:05] Guard #10 begins shift',
'[1518-11-03 00:24] falls asleep',
'[1518-11-03 00:29] wakes up',
'[1518-11-04 00:02] Guard #99 begins shift',
'[1518-11-04 00:36] falls asleep',
'[1518-11-04 00:46] wakes up',
'[1518-11-05 00:03] Guard #99 begins shift',
'[1518-11-05 00:45] falls asleep',
'[1518-11-05 00:55] wakes up]']

def convert_input(a_list):
  converted_schedule = {}
  for item in a_list:
    parsed_item = item.replace('[','').split('] ')
    converted_schedule[parsed_item[0]] = parsed_item[1]
  return converted_schedule

def order_schedule(a_schedule):
  ordered_schedule = OrderedDict()
  schedule_keys = a_schedule.keys()
  schedule_keys.sort()
  for item in schedule_keys:
    ordered_schedule[item] = a_schedule[item]
  return ordered_schedule

def sleep_by_guard(some_sched):
  fmt = '%Y-%m-%d %H:%M'
  current_sched = OrderedDict()
  falls_asleep = ''
  wakes_up = ''
  for x in some_sched:
    if 'Guard' in some_sched[x]:
      current_guard = some_sched[x].split(' ')[1]
      if current_guard not in current_sched:
        current_sched[current_guard] = { 'sleep_time': 0,
                                         'sleep_interval': [] }
        interval = []
    if 'falls' in some_sched[x]:
      falls_asleep = datetime.strptime(x, fmt)
      interval.append(falls_asleep.minute)
    if 'wakes' in some_sched[x]:
      wakes_up = datetime.strptime(x, fmt)
      interval.append(wakes_up.minute)
      current_sched[current_guard]['sleep_time'] += int(round((wakes_up - falls_asleep).total_seconds() / 60))
      current_sched[current_guard]['sleep_interval'].append(interval)
      interval = []
  return current_sched

def get_max_sleeper(sleep_totals_dict):
  max_sleep = 0
  guard = ''
  for sleep_total in sleep_totals_dict:
    if sleep_totals_dict[sleep_total]['sleep_time'] > max_sleep:
      max_sleep = sleep_totals_dict[sleep_total]['sleep_time']
      guard = sleep_total
  return guard

def get_most_common_minute(sleep_interval_dict, guard_id):
  if guard_id:
    sleep_intervals = sleep_interval_dict[guard_id]['sleep_interval']
  minute_counts = {}
  for i in range(0, 60):
    minute_counts[i] = 0
  for sleep_interval in sleep_intervals:
    for x in range(sleep_interval[0], sleep_interval[1]):
      minute_counts[x] += 1
  return minute_counts

def get_max_minute(sleep_minutes_dict):
  max_minute = 0
  max_count = 0
  for minutes in sleep_minutes_dict:
    if sleep_minutes_dict[minutes] > max_count:
      max_count = sleep_minutes_dict[minutes]
      max_minute = minutes
  return max_minute

def id_x_minute(guard_id, most_common_minute):
  return int(guard_id.replace('#', '')) * most_common_minute

#for p2 also
output = convert_input(schedule)
ordered_output = order_schedule(output)
guard_schedules = sleep_by_guard(ordered_output)

#for p1 only
max_sleeper = get_max_sleeper(guard_schedules)
overlapping_minutes = get_most_common_minute(guard_schedules, max_sleeper)
most_freq_minute = get_max_minute(overlapping_minutes)

# print id_x_minute(max_sleeper, most_freq_minute) #72925

#p4, p2
#get minute counts for every guard
def get_minute_counts_all_guards(sleep_interval_dict):
  minute_counts = {}
  for guard in sleep_interval_dict:
    if guard not in minute_counts:
        minute_counts[guard] = {}
    for i in range(0, 60):
      minute_counts[guard][i] = 0
  for guard in sleep_interval_dict:
    for interval in sleep_interval_dict[guard]['sleep_interval']:
      for x in range(interval[0], interval[1]):
        minute_counts[guard][x] += 1
  return minute_counts

def get_max_count_all_guards(minute_counts_dict):
  count_per_guard = {}
  for guard in minute_counts_dict:
    #call get_max_count_one_guard to get minute and max count for this guard
    count_per_guard[guard] = get_max_count_one_guard(minute_counts_dict[guard])
  return count_per_guard

def get_max_count_one_guard(minute_count_dict):
  most_freq_minute = 0
  max_count = 0
  for minute in minute_count_dict:
    if minute_count_dict[minute] > max_count:
      most_freq_minute = minute
      max_count = minute_count_dict[minute]
  return { 'count': max_count, 'minute': most_freq_minute }

def get_most_common_minute_all_guards(minute_counts_all_guards):
  max_count = 0
  max_minute = 0
  guard_id = ''
  for guard in minute_counts_all_guards:
    if minute_counts_all_guards[guard]['count'] > max_count:
      max_count = minute_counts_all_guards[guard]['count']
      max_minute = minute_counts_all_guards[guard]['minute']
      guard_id = guard
  return guard_id, max_minute

#count of minutes for each guard
minute_counts_all_guards = get_minute_counts_all_guards(guard_schedules)
all_guard_max_minutes = get_max_count_all_guards(minute_counts_all_guards)
guard_id, max_minute = get_most_common_minute_all_guards(all_guard_max_minutes)
#final result
p4_final_result = id_x_minute(guard_id, max_minute)
# print p4_final_result