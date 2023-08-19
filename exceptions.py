class NameNotCapitalised(Exception):
    """
    The stations' origin or destination wasn't fully capitalised.
    Stations should be formatted as such:\n
    `GBCDF` for Cardiff Central\n
    `GBQQM` for Manchester Piccadilly
    """
    pass

class NameWrongLength(Exception):
    """
    The station name provided is not 5 characters long.
    """
    pass