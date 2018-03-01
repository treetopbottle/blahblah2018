#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as in_file:
    nr_rows, nr_columns, nr_vehicles, nr_rides, ride_bonus, nr_simulation_steps = [int(i) for i in next(in_file).strip().split(' ')]

    rides = []
    for line in in_file:
        a, b, x, y, earliest_start, latest_finish = [int(i) for i in line.strip().split(' ')]
        ride = [(a,b), (x,y), earliest_start, latest_finish]
        rides.append(ride)

    for i in range(min(nr_rides, nr_vehicles)):
        print(1, i)
