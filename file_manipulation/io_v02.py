#!/usr/bin/env python3
file = open("people.csv")

for line in file:
    print("Name: {}, Age: {}".format(*line.split(",")))
file.close()
