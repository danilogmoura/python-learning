#!/usr/bin/env python3
file = open("people.csv")
data = file.read()
file.close()

for line in data.splitlines():
    print("Nname: {}, Age: {}".format(*line.split(",")))
