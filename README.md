# Train Time Finder For TFW Services 

## What is this?
This is a python script that uses Transport For Wales' API to get train arrival and 
departure times.

## How do I use this?
`python3 trainTimes.py <origin> <destination> <time> <date>`
`trainTimes.py` also serves as an example as to how the library is used.

| Attribute | Type |
|-----------| -----|
| `origin`  | `str`|
| `destination` | `str` |
| `time` | `str` NOTE: this MAY change in the future.|
| `date` | `str` NOTE: this MAY change to `datetime` in the future.|

## Examples 

```py
>>> import station
>>> station = station.Departures("GBCDF", "GBQQM", "2023-10-10", "12:00")
>>> station
<station.Departures object at 0x7f296cd40b50>
```
Station returns a `station.Departures` object. `station.legs` returns the departures 
from `GBCDF` to `GBQQM`.

```py
>>> station.legs
[{'sequence': '0', 'travelSegmentID': 'LS_1_0_TS_0', 'type': 'TRAIN', 'originTravelPoint': 
{'origin': 'GBCDF', 'type': 'STATION'}, 'destinationTravelPoint': 
{'origin': 'GBQQM', 'type': 'STATION'}, 
'departureDateTime': '2023-10-10T11:53:00', 
'arrivalDateTime': '2023-10-10T15:15:00', ...
>>>
```

## Why did you make this?
Transport For Wales' mobile app takes way too long to load, especially if all I'm doing 
is checking the time in which one train arrives at the station. This is a lot faster for 
me.