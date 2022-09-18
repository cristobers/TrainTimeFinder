from requests import get, exceptions
from getStationNamesAPI import getStationNames

def getTrainTimes(origin: str, destination: str, today: str, time: str) -> []:
    
    if len(origin) > 5:
        origin = getStationNames(origin) 

    if len(destination) > 5:
        destination = getStationNames(destination)

    try:
        r = get(f"https://tickets.trc.cymru/api/v1/silverrail/ticketsearch?token=Ir00ktJ11ZwvdSoNX79E&origin={origin}&destination={destination}&outboundDate={today}&outboundTime={time}&timeWindowInbound=departure&timeWindowOutbound=departure&ticketType=single&earlierSearch=false&adult=1&child=0&tfwRestricted=false&channelCode=WEB")
        return([t["travelSegments"][0] for t in r.json()["legs"][0]["legSolution"]])
    except KeyError as e:
        print(f"An error has occurred to do with: {e}, You may have misspelled one of the stations names or you've tried to look at train times in the past (you may have supplied a time in the past and forgotten a date)")        
    except exceptions.RequestException as e:
        print(f"An error has occured, {e} this may have something to do with either your internet connection or the Transport For Wales API.") 


