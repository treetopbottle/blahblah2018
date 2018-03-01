#!/usr/bin/env bash

./solution.py input/a_example.in        > output/a_example.in &
./solution.py input/b_should_be_easy.in > output/b_should_be_easy.in &
./solution.py input/c_no_hurry.in       > output/c_no_hurry.in &
./solution.py input/d_metropolis.in     > output/d_metropolis.in &
./solution.py input/e_high_bonus.in     > output/e_high_bonus.in &

wait

