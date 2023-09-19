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
| `time` | `str` |
| `date` | `str` |

NOTE: both `time` and `date` are subject to change in the future, mostly `date`, which 
is likely to change to `datetime`.

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
{'origin': 'GBQQM', 'type': 'STATION'}, 'departureDateTime': '2023-10-10T11:53:00', 
'arrivalDateTime': '2023-10-10T15:15:00', ...
>>>
```

## Why did you make this?
At the time of writing this (almost two years ago) the Transport For Wales app was VERY
slow, as such, this was a lot faster if all I was doing was remembering when my 
train was supposed to depart.
