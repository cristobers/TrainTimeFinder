import requests

def GetStationNames(user_input):
	r = requests.get('https://tfw.wales/api/silverrail-stations/find/{}'.format(user_input))
	counter = 0
	station_name = str(r.json()[counter]['name'])
	if station_name != user_input:
		counter += 1
	else:
		return str(r.json()[counter]['sr_code'])
