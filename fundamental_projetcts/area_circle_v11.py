#!/usr/bin/env python3
from math import pi
import sys


def circle(radius):
    return pi * float(radius) ** 2


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Is necessary to inform the radius of circle.")
        print("Usage: {} <radius>".format(sys.argv[0].split("/")[-1]))
    else:
        radius = sys.argv[1]
        area = circle(radius)
        print("Area of circle with radius", radius, "is", area)
