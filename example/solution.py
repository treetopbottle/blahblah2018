#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as in_file:
    rows, columns, min_ingredients, max_cells = [int(i) for i in next(in_file).split(' ')]
    print(rows, columns, min_ingredients, max_cells)

    pizza = {}
    for i,row in enumerate(in_file):
        for j,square in enumerate(row.strip()):
            pizza[i,j] = square
    print(pizza)
