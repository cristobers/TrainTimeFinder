#!/usr/bin/env python3

import requests, argparse
from time import gmtime, strftime
from datetime import date
from getStationNamesAPI import getStationNames
from getTrainTimesAPI import getTrainTimes

parser = argparse.ArgumentParser()
parser.add_argument("-o", "-O", help="origin station")
parser.add_argument("-d", "-D", help="destination station")
args = parser.parse_args()

today = date.today().strftime('%Y-%m-%d')
time = strftime("%H:%M", gmtime())

origin = getStationNames(args.o) 
destination = getStationNames(args.d) 

print(args.o, "-->", args.d, "\n")
for time in getTrainTimes(origin, destination, today, time):
    departureTime = time["travelSegments"][0]["departureDateTime"][11:]
    arrivalTime = time["travelSegments"][0]["arrivalDateTime"][11:]
    print(departureTime, "\t", arrivalTime)