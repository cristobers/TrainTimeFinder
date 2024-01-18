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
        
        # Returns the API variant of the station name if the API response field ['name']
        # is equal to the stationName.
        return ''.join([x['sr_code'] for x in resp.json() if x['name'] == stationName])
    except requests.exceptions.HTTPError as e:
        return str(e)

class Departures:
    def __init__(self, origin: str, destination: str, date: str, time: str, optional_args: dict = None):
        # self.data returns the raw data from the TFW API call, this is used internally.
        self.data = self.departures(origin, destination, date, time, optional_args)
        self.legs = self.legs()

    def legs(self):
        """
        Returns the journeys from origin station to destination station.
        """
        temp = []
        for elem in self.data["legs"][0]["legSolution"]:
            temp.append(elem["travelSegments"][0])
        return temp

    def departures(self, origin: str, destination: str, date: str, time: str, optional_args: dict) -> dict:
        """
        Grabs train departure times.
        """
        if type(origin) != str or type(destination) != str:
            raise TypeError("Station names should be of type str.")

        if len(origin) != 5 or len(destination) != 5:
            raise NameWrongLength("Station names should be 5 characters long,")

        if origin != origin.upper() or destination != destination.upper():
            raise NameNotCapitalised("Station names need to be fully capitalised.")
        try:
            if optional_args == None or len(optional_args) <= 0:
                resp = requests.get(TicketSearchURL(origin, destination, date, time))
            else:
                child, adult, earlier_search, ticket_type = optional_args.values()
                resp = requests.get(TicketSearchURL(origin, destination, date, time, 
                                                    ticket_type,
                                                    earlier_search,
                                                    child, 
                                                    adult))
            return resp.json()
        except requests.exceptions.HTTPError as e:
            print(e)
