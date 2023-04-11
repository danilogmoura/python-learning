#!/usr/bin/env python3

with open("people.csv") as file:
    with open("people.txt", "w") as output:
        for line in file:
            people = line.strip().split(",")
            print("Name: {}, Age: {}".format(*people), file=output)

if file.closed:
    print("File has already been closed!")

if output.closed:
    print("The output file has already been closed!")
