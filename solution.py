#!/usr/bin/env python3

import sys
import collections


def find_best_ride(rides, rides_left, position, time, bonus):
    min_wait_time = 9999999
    best_ride = -1
    best_pos = (0,0)
    best_time = 0
    for ride in rides_left:
        (a, b), (x, y), earliest_start, latest_finish = rides[ride]
        to_ride_dist = abs(position[0]-a) + abs(position[1]-b)
        ride_dist = abs(a-x) + abs(b-y)
        possible = latest_finish > time + to_ride_dist + ride_dist
        if possible:
            wait_to_start = earliest_start-time
            wait_time = max(to_ride_dist, wait_to_start)
            if wait_to_start >= 0: # bonus!!
                bonus = 1 + max(0.001, float(bonus) / 15)
                wait_time = float(wait_time) / bonus
            if wait_time < min_wait_time:
                best_pos = (x, y)
                best_time = ride_dist + max(earliest_start, time+to_ride_dist)
                best_ride = ride
                min_wait_time = wait_time
    if best_ride >= 0:
        rides_left.remove(best_ride)
    return best_ride, best_pos, best_time


with open(sys.argv[1]) as in_file:
    nr_rows, nr_columns, nr_vehicles, nr_rides, bonus, nr_simulation_steps = [int(i) for i in next(in_file).strip().split(' ')]

    rides = []
    rides_left = set()
    for nr,line in enumerate(in_file):
        a, b, x, y, earliest_start, latest_finish = [int(i) for i in line.strip().split(' ')]
        ride = [(a,b), (x,y), earliest_start, latest_finish]
        rides.append(ride)
        rides_left.add(nr)

    vehicle_rides = collections.defaultdict(list)
    for veh_nr in range(nr_vehicles):
        pos = (0,0)
        time = 0
        while True:
            positions_for_vehicle = []
            best_ride_nr, new_pos, new_time = find_best_ride(rides, rides_left, pos, time, bonus)
            if best_ride_nr < 0:
                break
            vehicle_rides[veh_nr].append(best_ride_nr)
            pos = new_pos
            time = new_time

    for i in range(nr_vehicles):
        v_r = vehicle_rides[i]
        print(len(v_r), ' '.join([str(i) for i in v_r]))

