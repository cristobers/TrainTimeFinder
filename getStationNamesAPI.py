import requests

def getStationNames(user_input):
    try:
        r = requests.get(f"https://tfw.wales/api/silverrail-stations/find/{user_input}").json()
        return [x["sr_code"] for x in r if x["name"] == user_input]
    except Exception as e:
        print("An error has occured: ", e)
