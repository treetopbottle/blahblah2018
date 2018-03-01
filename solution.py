#!/usr/bin/env python3

import sys
import collections


def find_best_ride(rides, rides_left, position, time):
    for ride in rides_left:
        (a, b), (x, y), earliest_start, latest_finish = rides[ride]
        to_ride_dist = abs(position[0]-a) + abs(position[1]-b)
        ride_dist = abs(a-x) + abs(b-y)
        possible = latest_finish > time + to_ride_dist + ride_dist
        if possible:
            rides_left.remove(ride)
            new_pos = (x, y)
            new_time = ride_dist + max(earliest_start, time+to_ride_dist)
            return ride, new_pos, new_time
    return -1, (0,0), 0


with open(sys.argv[1]) as in_file:
    nr_rows, nr_columns, nr_vehicles, nr_rides, ride_bonus, nr_simulation_steps = [int(i) for i in next(in_file).strip().split(' ')]

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
            best_ride_nr, new_pos, new_time = find_best_ride(rides, rides_left, pos, time)
            if best_ride_nr < 0:
                break
            vehicle_rides[veh_nr].append(best_ride_nr)
            pos = new_pos
            time = new_time

    for i in range(nr_vehicles):
        v_r = vehicle_rides[i]
        print(len(v_r), ' '.join([str(i) for i in v_r]))

