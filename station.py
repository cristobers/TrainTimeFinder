import requests
from const import *
from exceptions import NameNotCapitalised, NameWrongLength

def TicketSearchURL(origin: str, 
                    destination: str, 
                    outboundDate: str, 
                    outboundTime: str,
                    ticketType: str = "single",
                    earlierSearch: bool = False,
                    adult: int = 1,
                    child: int = 0) -> str:
    """
    Creates a URL suitable for the TFW API.
    """

    if ticketType not in ("single", "return"):
        raise Exception("Ticket type has to be either \"single\" or \"return\"")

    if type(adult) != int or type(child) != int:
        raise TypeError("Both the adult and child arguments need to be an int.")

    url = f"{TFW_TICKETS_BASE_API}{TFW_TICKET_SEARCH}&origin={origin}" \
    f"&destination={destination}&outboundDate={outboundDate}" \
    f"&outboundTime={outboundTime}&timeWindowInbound=departure" \
    f"&timeWindowOutbound=departure&ticketType={ticketType}" \
    f"&earlierSearch={earlierSearch}&adult={adult}&child={child}"
    return url

def name(stationName: str) -> str:
    """
    Gets the API variant of a train station's name from Transport For Wales' API.
    Returns the internal name as a string.
    """
    if type(stationName) != str:
        raise TypeError("Station name has to be of type str.")
    try:
        URL = f"{TFW_STATIONS_BASE_API}{TFW_FIND_STATIONS}{stationName}"
        resp = requests.get(URL)
        return ''.join(
            [x['sr_code'] for x in resp.json() if x['name'] == stationName])
    except requests.exceptions.HTTPError as e:
        return str(e)

class Departures:
    def __init__(self, origin: str, destination: str, date: str, time: str):
        self.data = self.departures(origin, destination, date, time)
        self.legs = self.legs()

    def legs(self):
        """
        Returns the journeys from origin station to destination station.
        """
        temp = []
        for elem in self.data["legs"][0]["legSolution"]:
            temp.append(elem["travelSegments"][0])
        return temp

    def departures(self, origin, destination, date, time) -> dict:
        """
        Grabs train departure times.
        """
        if type(origin) != str:
            raise TypeError("Origin station should be of type str.")
        elif type(destination) != str:
            raise TypeError("Destination station should be of type str.")

        if origin != origin.upper():
            raise NameNotCapitalised("Origin station needs to be capitalised.")
        elif destination != destination.upper():
            raise NameNotCapitalised("Destination station needs to be capitalised.")

        if len(origin) != 5:
            raise NameWrongLength("Origin station needs to be 5 characters long.")
        elif len(destination) != 5:
            raise NameWrongLength("Destination station needs to be 5 characters long.")

        try:
            resp = requests.get(TicketSearchURL(origin, destination, date, time))
            return resp.json()
        except requests.exceptions.HTTPError as e:
            print(e)
    
    def arrivals(self, origin: str, destination: str, date: str, time: str) -> dict:
        """
        Calls `self.departures()` but changes the position of the origin and destination
        stations.
        """
        return self.departures(self, destination, origin, date, time)
