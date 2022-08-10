#!/usr/bin/env python3

import argparse
from time import gmtime, strftime
from datetime import date
from getStationNamesAPI import getStationNames
from getTrainTimesAPI import getTrainTimes

parser = argparse.ArgumentParser()
parser.add_argument("-o", "-O", help="Origin Station")
parser.add_argument("-d", "-D", help="Destination Station")
args = parser.parse_args()

origin = args.o
destination = args.d

today = date.today().strftime('%Y-%m-%d')
time = strftime("%H:%M", gmtime())

print(args.o, "-->", args.d)
for time in getTrainTimes(origin, destination, today, time):
    departureTime = time["departureDateTime"][11:][:5]
    arrivalTime = time["arrivalDateTime"][11:][:5]
    print(departureTime, "\t", arrivalTime)
