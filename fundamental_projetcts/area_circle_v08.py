#!/usr/bin/env python3
from math import pi


def circle(radius):
    print("Area of circle is: ", pi * float(radius) ** 2)


if __name__ == "__main__":
    radius = input("Enter radius of circle: ")
    circle(radius)
