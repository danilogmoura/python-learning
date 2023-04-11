#!/usr/bin/env python3
import csv

with open('people.csv') as imputFile:
    for line in csv.reader(imputFile):
        print('Name: {}, Age: {}'.format(*line))
