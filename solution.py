#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as in_file:
    nr_rows, nr_columns, nr_vehicles, nr_rides, ride_bonus, nr_simulation_steps = [int(i) for i in next(in_file).strip().split(' ')]

    rides = []  # TODO: prioritize the rides
    weighted_rides = set()
    for nr,line in enumerate(in_file):
        a, b, x, y, earliest_start, latest_finish = [int(i) for i in line.strip().split(' ')]
        ride = [(a,b), (x,y), earliest_start, latest_finish]
        rides.append(ride)
        weighted_rides.add(nr)

    vehicle_rides = []
    for i in range(nr_vehicles):
        best_ride = min(weighted_rides)
        weighted_rides.remove(best_ride)
        vehicle_rides.append([best_ride])

    for v_r in vehicle_rides:
        print(len(v_r), ' '.join([str(i) for i in v_r]))

