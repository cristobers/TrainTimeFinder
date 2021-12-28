# Train Time Finder For TFW Services 

## How do I use this?
- `-h` Displays the help menu
- `-o` Is your origin station (the one you're at)
- `-d` Is your destination station (the one you're going to)

## What is this?
This is a python script that uses Transport For Wales' API to get the train arrival and departure times for Transport For Wales' journeys.

## Why did you make this?
I got frustrated with Transport For Wales' mobile interface for finding train times. 

## How do I add more stations?
If you go into `trainTimes.py` you'll see a dictionary called `stations`. Within this dictionary you add both the stations code (the one that the TFW api uses) and also the name of the station itself. If you're confused on how to add more stations, have a look at how the other stations are formatted. 
```python
stations = {
	"Pye Corner":"GBPYE"
	...
	"<station name>":"<TFW API internal station name>"
}
``` 
