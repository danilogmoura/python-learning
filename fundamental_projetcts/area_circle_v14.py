#!/usr/bin/env python3
from math import pi
import sys
import errno


def help():
    print("Is necessary to inform the radius of circle.")
    print("Usage: {} <radius>".format(sys.argv[0].split("/")[-1]))


def circle(radius):
    return pi * float(radius) ** 2


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print("The radius must be a numeric value.")
        sys.exit(errno.EINVAL)

    radius = sys.argv[1]
    area = circle(radius)
    print("Area of circle with radius", radius, "is", area)
