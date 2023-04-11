#!/usr/bin/env python3
try:
    file = open("people.csv")

    for line in file:
        print("Name: {}, Age: {}".format(*line.strip().split(",")))
finally:
    file.close()

if file.closed:
    print("File has already been closed!")
