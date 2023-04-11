#!/usr/bin/env python3

with open("people.csv") as file:
    for line in file:
        print("Name: {}, Age: {}".format(*line.strip().split(",")))

if file.closed:
    print("File has already been closed!")
