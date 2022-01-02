import requests

def GetStationNames(user_input):
    # maybe add a test case for if there's a bad response (404, 403 etc.)
    r = requests.get(f'https://tfw.wales/api/silverrail-stations/find/{user_input}').json()
	for x in r:
		if x['name'] == user_input:
			return x['sr_code']
