# Train Time Finder For TFW Services 

![beautiful gif of the script working](train.gif)

## What is this?
This is a python script that uses Transport For Wales' API to get train arrival and departure times.

## How do I use this?
- `-h` Displays the help menu
- `-o` Is your Origin Station (the one you're at)
- `-d` Is your Destination Station (the one you're going to)
- `-D, -date` Is for checking times on a specific date
- `-t` Is for checking times at a specific time 

If you're going to use the date and time arguments, make sure to not set either one to a time or date within the past, otherwise the script will throw an error.

## Why did you make this?
Transport For Wales' mobile app takes way too long to load, especially if all I'm doing is checking the time in which one train arrives at the station. This is a lot faster (for me anyways).
