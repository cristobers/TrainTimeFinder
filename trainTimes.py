import station
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("o", help="Origin", metavar='\b')
parser.add_argument("d", help="Destination", metavar='\b')
parser.add_argument("t", help="Time", metavar='\b')
parser.add_argument("D", help="Date", metavar='\b')
args = parser.parse_args()

origin, destination, time, date = args.o, args.d, args.t, args.D
correct_format = lambda a : len(a) == 5 and a[:2] == "GB"

# If correct_format() fails, change the stations name to its API counterpart.
if not correct_format(origin):
    origin = station.name(args.o)
if not correct_format(destination):
    destination = station.name(args.d)

station = station.Departures(origin, destination, date, time)
print(f"{origin} --> {destination}")
for leg in station.legs:
    print(leg["departureDateTime"], leg["arrivalDateTime"])