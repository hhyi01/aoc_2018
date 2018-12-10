#p7
from collections import OrderedDict
import sys

with open('/Users/hyi/Desktop/aoc_2018/Day 7/p_07_input.txt') as f:
    p7_input = f.readlines()

p7_input = [x.strip() for x in p7_input]

sample_input = ['Step C must be finished before step A can begin.',
'Step C must be finished before step F can begin.',
'Step A must be finished before step B can begin.',
'Step A must be finished before step D can begin.',
'Step B must be finished before step E can begin.',
'Step D must be finished before step E can begin.',
'Step F must be finished before step E can begin.']

def get_step(line):
    return line.split(' ')[7]

def get_requirement(line):
    return line.split(' ')[1]

def get_steps_dependencies(instructions, steps):
    for task in instructions:
        step = get_step(task)
        steps[step].append(get_requirement(task))
    return steps

def get_all_steps(instructions):
    #key is step, value is step requirement
    steps = {}
    for task in instructions:
        step = get_step(task)
        requirement = get_requirement(task)
        if step not in steps:
            steps[step] = []
        if requirement not in steps:
            steps[requirement] = []
    return steps

def get_order_steps(steps):
    steps_in_order = OrderedDict()
    while len(steps) > 0:
        if len(steps_in_order) == 0:
            first_step = get_next_step(steps)
            steps_in_order[first_step] = 'done'
            steps.pop(first_step, None)
        else:
            steps = remove_fulfilled_steps(steps_in_order, steps)
            next_step = get_next_step(steps)
            steps_in_order[next_step] = 'done'
            steps.pop(next_step, None)
    steps_executed = steps_in_order.keys()
    return ''.join(steps_executed)


def remove_fulfilled_steps(steps_done, steps_requirements):
    for step in steps_requirements:
        s = 0
        while s < len(steps_requirements[step]):
            index = 0
            if steps_requirements[step][s] in steps_done:
                steps_requirements[step].pop(s)
                index = s
            if index != 0:
                s = index
            else:
                s += 1
    return steps_requirements

def get_next_step(steps):
    steps_available = []
    for s in steps:
        if len(steps[s]) == 0:
            steps_available.append(s)
    steps_available.sort()
    return steps_available[0]

#p1
all_steps = get_all_steps(p7_input)
steps_with_requirements = get_steps_dependencies(p7_input, all_steps)
# all_steps_ordered = get_order_steps(steps_with_requirements)

#p2
step_labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def populate_step_times(labels):
    step_times = {}
    for i in range(0, len(labels)):
        step_times[labels[i]] = (i + 1) + 60
    return step_times

def get_next_steps(steps):
    steps_available = []
    for s in steps:
        if len(steps[s]) == 0:
            steps_available.append(s)
    steps_available.sort()
    return steps_available  

def available_worker(workers):
    free_worker = ''
    for worker in workers:
        if len(workers[worker]) == 0:
            free_worker = worker
    return free_worker

def create_workers(worker_numbers):
    workers = {}
    for x in range(1, worker_numbers + 1):
        #initialize workers with time 0
        workers[x] = {}
    return workers

def decrement_worker_time(workers):
    for worker in workers:
        for key in workers[worker]:
            if workers[worker][key] > 0:
                workers[worker][key] -= 1
    return workers

def get_min_wait_time(workers):
    min_wait_time = sys.maxint
    for worker in workers:
        for key in workers[worker]:
            if workers[worker][key] < min_wait_time:
                min_wait_time = workers[worker][key]
    return min_wait_time

def clear_old_steps(workers, steps_in_order):
    for worker in workers:
        for step in steps_in_order:
            if step in workers[worker] and workers[worker][step] == 0:
                workers[worker].pop(step, None)
    return workers

def remaining_seconds(workers):
    seconds = 0
    for worker in workers:
        for key in workers[worker]:
            if workers[worker][key] > seconds:
                seconds = workers[worker][key]
    return seconds

def get_order_time(steps, no_workers_assigned, step_times):
    steps_in_order = OrderedDict()
    workers = create_workers(no_workers_assigned)
    elapsed_seconds = 0
    time_to_wait = 0

    while len(steps) > 0:
        if time_to_wait == 0:
            steps = remove_fulfilled_steps(steps_in_order, steps)
            next_steps = get_next_steps(steps)
            for step in next_steps:
                worker = available_worker(workers)
                if worker != '':
                    workers[worker][step] = step_times[step]
                    steps_in_order[step] = 'done'
                    steps.pop(step, None)
        time_to_wait = get_min_wait_time(workers)
        elapsed_seconds += 1
        workers = decrement_worker_time(workers)
        time_to_wait -= 1
        workers = clear_old_steps(workers, steps_in_order)
        print 'next',len(steps_in_order)
        print 'seconds', elapsed_seconds
        print 'wait', time_to_wait
        print workers
    return elapsed_seconds

step_times = populate_step_times(step_labels)
# need steps_with_requirements from part 1
print get_order_time(steps_with_requirements, 5, step_times)
# print step_times



