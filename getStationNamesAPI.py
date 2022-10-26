from requests import get

def getStationNames(user_input: str) -> str:
    try:
        r = get(f"https://tfw.wales/api/silverrail-stations/find/{user_input}").json()
        return ''.join([x["sr_code"] for x in r if x["name"] == user_input])
    except Exception as e:
        print("An error has occured: ", e)
