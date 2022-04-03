import requests

def getStationNames(user_input):
    try:
        r = requests.get(f"https://tfw.wales/api/silverrail-stations/find/{user_input}").json()
        for x in r:
            if x["name"] == user_input:
                return x["sr_code"]
    except Exception as e:
        print("An error has occured: ", e)
