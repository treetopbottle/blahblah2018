#!/usr/bin/env bash

for input in $(find input/*); do
    echo $input;
    date;
    ./solution.py $input > "output/$input";
    date;
done;
