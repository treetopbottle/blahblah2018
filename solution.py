#!/usr/bin/env python3

import sys
import collections


def find_best_ride(rides, rides_left, position, time):
    # TODO find possible ride
    if len(rides_left) > 0:
        return rides_left.pop()
    return False


with open(sys.argv[1]) as in_file:
    nr_rows, nr_columns, nr_vehicles, nr_rides, ride_bonus, nr_simulation_steps = [int(i) for i in next(in_file).strip().split(' ')]

    rides = []
    rides_left = set()
    for nr,line in enumerate(in_file):
        a, b, x, y, earliest_start, latest_finish = [int(i) for i in line.strip().split(' ')]
        ride = [(a,b), (x,y), earliest_start, latest_finish]
        rides.append(ride)
        rides_left.add(nr)

    vehicle_position_times = []
    for i in range(nr_vehicles):
        vehicle_position_times.append([(0,0), 0])

    vehicle_rides = collections.defaultdict(list)
    ride_found = True
    while len(rides_left) > 0 and ride_found:
        print('----')
        ride_found = False
        for vehicle_number in range(nr_vehicles):
            pos, time = vehicle_position_times[vehicle_number]
            best_ride = find_best_ride(rides, rides_left, pos, time)
            if best_ride:
                vehicle_rides[vehicle_number].append(best_ride)
                ride_found = True

    for key in vehicle_rides:
        v_r = vehicle_rides[key]
        print(len(v_r), ' '.join([str(i) for i in v_r]))

