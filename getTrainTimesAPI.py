import requests

def getTrainTimes(origin, destination, today, time):
    r = requests.get(f"https://tickets.trc.cymru/api/v1/silverrail/ticketsearch?token=Ir00ktJ11ZwvdSoNX79E&origin={origin}&destination={destination}&outboundDate={today}&outboundTime={time}&timeWindowInbound=departure&timeWindowOutbound=departure&ticketType=single&earlierSearch=false&adult=1&child=0&tfwRestricted=false&channelCode=WEB")
    if r.status_code != 200:
        print("error with getting train times.") 
    else:
        return([t["travelSegments"][0] for t in r.json()["legs"][0]["legSolution"]])