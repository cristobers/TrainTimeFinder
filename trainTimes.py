#!/usr/bin/env python3

import sys
from argparse import ArgumentParser
from time import localtime, strftime
from datetime import date
from getTrainTimesAPI import getTrainTimes

parser = ArgumentParser()
parser.add_argument("-o", help="Origin Station", metavar='\b')
parser.add_argument("-d", help="Destination Station", metavar='\b')
parser.add_argument("-t", help="Specific Time, giving times in the past throws an error ( no time travelling allowed )", metavar='\b')
parser.add_argument("-date", "-D", help="Specific Date, months are formatted as such: 2022-09-18, months are zero-padded if they're < 10", metavar='\b')

args = parser.parse_args()
origin, destination, time, day, printed = args.o, args.d, args.t, args.date, False

if day is not None and day < date.today().strftime('%Y-%m-%d'):
    print("ERROR: You've tried to supply a date or time that is in the past.")
    sys.exit()
else:
    today = [date.today().strftime('%Y-%m-%d') if day is None else str(day)][0]

if time is None:
    time = strftime("%H:%M", localtime())
else:
    if len(str(time)) == 4 and str(time)[0] != '0':
        time = '0' + str(time)
    else:
        time = str(time)

print(args.o, "-->", args.d)
for time in getTrainTimes(origin, destination, today, time):
    departureTime = time["departureDateTime"][11:][:5]
    arrivalTime = time["arrivalDateTime"][11:][:5]
    transportType = time["type"]

    if transportType == "BUS" and printed == False:
        print("There may be disruptions on your journey, please check the Tansport For Wales app just to make sure. (bus replacements or otherwise)")
        printed = True

    print(departureTime, "\t", arrivalTime)
