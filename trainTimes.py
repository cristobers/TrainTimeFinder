#!/usr/bin/env python3
import requests, datetime, argparse
from time import gmtime, strftime

stations = {
        "Pye Corner":"GBPYE", 
        "Cardiff Central":"GBCDF", 
        "Trefforest":"GBTRF",
        "Pontyprydd":"GBPPD"
}

parser = argparse.ArgumentParser()
parser.add_argument("-o", "-O", help="origin station (where your joruney starts)")
parser.add_argument("-d", "-D", help="destination station (where you want to go)")
args = parser.parse_args()

today = datetime.date.today().strftime('%Y-%m-%d')
time = strftime("%H:%M", gmtime())

origin = stations[args.o] 
destination = stations[args.d] 

# url for api requests, this will probably have to be changed if and when TFW change their API.
url = 'https://tickets.trc.cymru/api/v1/silverrail/ticketsearch?token=Ir00ktJ11ZwvdSoNX79E&origin={origin}&destination={destination}&outboundDate={outbound_date}&outboundTime={out_time}&timeWindowInbound=departure&timeWindowOutbound=departure&ticketType=single&earlierSearch=false&adult=1&child=0&tfwRestricted=false&channelCode=WEB'.format(outbound_date = today, out_time = time, origin = origin, destination = destination)
r = requests.get(url)

print("Departs from",args.o , "\t", "Arrives At", args.d)
for x in range(0, 5):
    try:
        departureTime = str(r.json()["legs"][0]["legSolution"][x]["travelSegments"][0]["departureDateTime"])[11:]
        arrivalTime = str(r.json()["legs"][0]["legSolution"][x]["travelSegments"][0]["arrivalDateTime"])[11:]
        print(departureTime, "\t","\t","\t", arrivalTime)
    except IndexError:
        break
