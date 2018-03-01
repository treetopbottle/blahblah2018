#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as in_file:
    nr_rows, nr_columns, nr_vehicles, nr_rides, ride_bonus, nr_simulation_steps = [int(i) for i in next(in_file).strip().split(' ')]

    for line in in_file:
        start_row, start_column, finish_row, finish_column, earliest_start, latest_finish = [int(i) for i in line.strip().split(' ')]

