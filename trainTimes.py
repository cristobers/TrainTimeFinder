#!/usr/bin/env python3

from argparse import ArgumentParser
from time import gmtime, strftime
from datetime import date
from getTrainTimesAPI import getTrainTimes

parser = ArgumentParser()
parser.add_argument("-o", help="Origin Station", metavar='\b')
parser.add_argument("-d", help="Destination Station", metavar='\b')
parser.add_argument("-t", help="Specific Time, giving times in the past throws an error ( no time travelling allowed )", metavar='\b')
parser.add_argument("-date", "-D", help="Specific Date, months are formatted as such: 2022-09-18, months are zero-padded if they're < 10", metavar='\b')
args = parser.parse_args()

origin, destination, time, day = args.o, args.d, args.t, args.date
today = [date.today().strftime('%Y-%m-%d') if day is None else str(day)][0]

if time is None:
    time = strftime("%H:%M", gmtime())
else:
    if len(str(time)) == 4 and str(time)[0] != '0':
        time = '0' + str(time)
    else:
        time = str(time)

print(args.o, "-->", args.d)
for time in getTrainTimes(origin, destination, today, time):
    departureTime = time["departureDateTime"][11:][:5]
    arrivalTime = time["arrivalDateTime"][11:][:5]
    print(departureTime, "\t", arrivalTime)