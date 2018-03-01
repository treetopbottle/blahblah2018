#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as in_file:
    nr_rows, nr_columns, nr_vehicles, nr_rides, ride_bonus, nr_simulation_steps = [int(i) for i in next(in_file).strip().split(' ')]
    print(nr_rows, nr_columns, nr_vehicles, nr_rides, ride_bonus, nr_simulation_steps)
    print(type(nr_rows))
