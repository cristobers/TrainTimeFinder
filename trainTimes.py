#!/usr/bin/env python3
import requests, argparse
from time import gmtime, strftime
from datetime import date
from getStationNames import GetStationNames

parser = argparse.ArgumentParser()
parser.add_argument("-o", "-O", help="origin station")
parser.add_argument("-d", "-D", help="destination station")
args = parser.parse_args()

today = date.today().strftime('%Y-%m-%d')
time = strftime("%H:%M", gmtime())

origin = GetStationNames(args.o) 
destination = GetStationNames(args.d) 

# this url will have to be changed if and when TFW change their API.
r = requests.get(f'https://tickets.trc.cymru/api/v1/silverrail/ticketsearch?token=Ir00ktJ11ZwvdSoNX79E&origin={origin}&destination={destination}&outboundDate={today}&outboundTime={time}&timeWindowInbound=departure&timeWindowOutbound=departure&ticketType=single&earlierSearch=false&adult=1&child=0&tfwRestricted=false&channelCode=WEB').json()['legs'][0]['legSolution']

print("Departs from",args.o, "\t", "Arrives At", args.d)
for x in r:
	try:
		departureTime = x["travelSegments"][0]["departureDateTime"][11:]
		arrivalTime = x["travelSegments"][0]["arrivalDateTime"][11:]
		print(departureTime, "\t"*3, arrivalTime)
	except IndexError:
		break
