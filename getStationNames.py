import requests

def GetStationNames(user_input):
	r = requests.get('https://tfw.wales/api/silverrail-stations/find/{}'.format(user_input))
	return r.json()
