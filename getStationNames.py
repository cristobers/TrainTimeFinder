import requests

def GetStationNames(user_input):
	try:
		r = requests.get('https://tfw.wales/api/silverrail-stations/find/{}'.format(user_input))
		r.raise_for_status()
	except requests.exceptions.RequestException as e:
		raise SystemExit(e)
	counter = 0
	try:
		station_name = str(r.json()[counter]['name'])
		
		if station_name != user_input:
			counter += 1
		else:
			return str(r.json()[counter]['sr_code'])
	except ValueError:
		print('value error, either you didnt spell the station correctly or you didnt type in the correct name of the station.')
