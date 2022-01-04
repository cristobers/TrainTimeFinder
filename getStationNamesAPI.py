import requests

def getStationNames(user_input):
    # maybe add try/except for http errors 
    r = requests.get(f"https://tfw.wales/api/silverrail-stations/find/{user_input}").json()
    for x in r:
        if x["name"] == user_input:
            return x["sr_code"]
