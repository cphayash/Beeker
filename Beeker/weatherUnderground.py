#! /usr/bin/python

import sys
import urllib
import json
import os
from pprint import pprint
from respond import respond


# Define the Location class
#
# This class is called within the subsequent WeatherMetrics
# class, as WeatherMetrics contains 2 locations.
# Location 1: Display Location
# Location 2: Observation Location
class Location(object):
	city = ""
	state = ""
	zipCode = ""
	country = ""
	elevation = ""
	longitude = ""
	latitude = ""
	timezone = ""
	
	def __init__(self, jsonData, kind):
		self.city = jsonData["city"]
		self.state = jsonData["state"]
		self.country = jsonData["country"]
		self.elevation = jsonData["elevation"]
		self.longitude = jsonData["longitude"]
		self.latitude = jsonData["latitude"]
		if kind == "display_location":
			self.zipCode = jsonData["zip"]
		



# Define the WeatherMetrics class
# 		
# This class is called 
class WeatherMetrics(object):
	local_tz_short = ""
	local_tz_long = ""
	local_tz_offset = ""
	weather = ""
	temperature_string = ""
	temp_f = ""
	temp_c = ""
	relative_humidity = ""
	wind_string = ""
	wind_dir = ""
	wind_degrees = ""
	wind_mph = ""
	wind_gust_mph = ""
	wind_kph = ""
	wind_gust_kph = ""
	pressure_mb = ""
	pressure_in = ""
	pressure_trend = ""
	dewpoint_string = ""
	dewpoint_f = ""
	dewpoint_c = ""
	heat_index_string = ""
	heat_index_f = ""
	heat_index_c = ""
	windchill_string = ""
	windchill_f = ""
	windchill_c = ""
	feelslike_string = ""
	feelslike_f = ""
	feelslike_c = ""
	visibility_mi = ""
	visibility_km = ""
	solar_radiation = ""
	uv = ""
	precip_1hr_string = ""
	precip_1hr_in = ""
	precip_1hr_metric = ""
	precip_today_string = ""
	precip_today_in = ""
	precip_today_metric = ""

	curLocation = None
	observationLocation = None


	def __init__(self, weatherData):
		self.local_tz_short = weatherData["local_tz_short"]
		self.local_tz_long = weatherData["local_tz_long"]
		self.local_tz_offset = weatherData["local_tz_offset"]
		self.weather = weatherData["weather"].lower()
		self.temp_f = weatherData["temp_f"]
		self.temp_c = weatherData["temp_c"]
		self.temperature_string = u"{} \xb0F ({} \xb0C)".format(self.temp_f, self.temp_c)
		self.relative_humidity = weatherData["relative_humidity"]
		self.wind_string = weatherData["wind_string"]
		self.wind_dir = weatherData["wind_dir"]
		self.wind_degrees = weatherData["wind_degrees"]
		self.wind_mph = weatherData["wind_mph"]
		self.wind_gust_mph = weatherData["wind_gust_mph"]
		self.wind_kph = weatherData["wind_kph"]
		self.wind_gust_kph = weatherData["wind_gust_kph"]
		self.pressure_mb = weatherData["pressure_mb"]
		self.pressure_in = weatherData["pressure_in"]
		self.pressure_trend = weatherData["pressure_trend"]
		self.dewpoint_string = weatherData["dewpoint_string"]
		self.dewpoint_f = weatherData["dewpoint_f"]
		self.dewpoint_c = weatherData["dewpoint_c"]
		self.heat_index_string = weatherData["heat_index_string"]
		self.heat_index_f = weatherData["heat_index_f"]
		self.heat_index_c = weatherData["heat_index_c"]
		self.windchill_string = weatherData["windchill_string"]
		self.windchill_f = weatherData["windchill_f"]
		self.windchill_c = weatherData["windchill_c"]
		self.feelslike_string = weatherData["feelslike_string"]
		self.feelslike_f = weatherData["feelslike_f"]
		self.feelslike_c = weatherData["feelslike_c"]
		self.visibility_mi = weatherData["visibility_mi"]
		self.visibility_km = weatherData["visibility_km"]
		self.solar_radiation = weatherData["solarradiation"]
		self.UV = weatherData["UV"]
		self.precip_1hr_string = weatherData["precip_1hr_string"]
		self.precip_1hr_in = weatherData["precip_1hr_in"]
		self.precip_1hr_metric = weatherData["precip_1hr_metric"]
		self.precip_today_string = weatherData["precip_today_string"]
		self.precip_today_in = weatherData["precip_today_in"]
		self.precip_today_metric = weatherData["precip_today_metric"]

		self.curLocation = Location(weatherData["display_location"], "display_location")
		self.observationLocation = Location(weatherData["observation_location"], "observation_location")
		# self.weatherSummary = self.WeatherSummary()
	
	

class WeatherSummary(WeatherMetrics):
	def __init__(self):
		self.city = self.curLocation.city
		self.state = super().curLocation.state
		self.country = super().curLocation.country
		self.wind_mph = super().wind_mph
		self.wind_gust_mph = super().wind_gust_mph
		self.feelslike_f = super().feelslike_f
		self.feelslike_string = super().feelslike_string
		self.visibility_mi = super().visibility_mi
		self.weather = super().weather
	# class WeatherSummary(object):
	# 	def __init__(self):
	# 		self.city = self.super.curLocation.city
	# 		self.state = super().curLocation.state
	# 		self.country = super().curLocation.country
	# 		self.wind_mph = super().wind_mph
	# 		self.wind_gust_mph = super().wind_gust_mph
	# 		self.feelslike_f = super().feelslike_f
	# 		self.feelslike_string = super().feelslike_string
	# 		self.visibility_mi = super().visibility_mi
	# 		self.weather = super().weather

# Use the URL passed in and get JSON data from weatherUnderground.
# Refine list (where the [:-1]) is, concatenate (join) to string type.
# Load as JSON and use "current_observation" to instantiate
# a WeatherMetrics object and return it
def getMetrics(URL):
	curURL = urllib.urlopen(URL)
	rawData = [line[:-1] for line in curURL.readlines()]
	weatherData = "".join(rawData)

	weatherJSON = json.loads(weatherData)
	curWeather = weatherJSON["current_observation"]

	return WeatherMetrics(curWeather)


# Use loosely formatted city name, which is formatted
# for use in URL string (ex: change " " to "%20").
# Search weatherUnderground for matching city names
# and return the results JSON
def findLocation(locationString, searchPrefix):
	sample_url = "http://autocomplete.wunderground.com/aq?query=query"

	locationList = locationString.split(" ")
	locationString = "%20".join(locationList)
	searchURL = "{}{}".format(searchPrefix, locationString)

	searchReturn = urllib.urlopen(searchURL)
	searchData = [line[:-1] for line in searchReturn.readlines()]
	locationData = "".join(searchData).replace("\t", "") + "}"
	# print searchData
	# print locationData
	locationJSON = json.loads(locationData)

	return locationJSON


# Merely a container class to clean up the appearance of 
# the rest of the script. 
# It's not important to know the details of the enclosed
# information, so it's abstracted away
class API_Data(object):
	def __init__(self):
		self.apiKey = None
		self.myPath = os.path.dirname(os.path.realpath(__file__))
		self.subdir = "weatherUnderground"
		self.newPath = "/".join([self.myPath, self.subdir, "apiData.json"])
		# self.rawData = None
		self.jsonData = None

		with open(self.newPath, "r") as myFile:
			self.rawData = myFile.readlines()
			self.jsonData = json.loads(" ".join(self.rawData))

		self.pretext = self.jsonData["pretext"]
		self.posttext = self.jsonData["posttext"]
		self.apiKey = self.jsonData["apiKey"]
		self.town = "{}.json".format(self.jsonData["hometown"])
		self.state = self.jsonData["homestate"]
		self.searchPrefix = self.jsonData["search_prefix"]
		self.fullURL = "/".join([self.pretext, self.apiKey, self.posttext, self.state, self.town])



def printSummary(weatherMetrics):
	print "\n\nweatherMetrics:"
	for key, val in vars(weatherMetrics).iteritems():
		print "{}: {}".format(key, val)

	print "\n\ncurLocation:"
	for key, val in vars(weatherMetrics.curLocation).iteritems():
		print "{}: {}".format(key, val)

	print "\n\nobservationLocation:"
	for key, val in vars(weatherMetrics.observationLocation).iteritems():
		print "{}: {}".format(key, val)


# Print data returned by searchCity() in JSON format
def printCityData(cityData):
	print "cityData:"
	for key, val in cityData.iteritems():
		print "\n{}: {}".format(key, val)


# Take JSON from findLocation() function, format it to separate
# City and State, then return as a dictionary
def searchCity(cityName):
	initialData = findLocation(cityName, apiData.searchPrefix)["RESULTS"]
	# cityData = findLocation(cityName, apiData.searchPrefix)["RESULTS"][0]
	if len(initialData) == 0:
		cityData = {"name": "No Data, No Data"}
	else:
		cityData = initialData[0]
	# print initialData
	# sys.exit(0)

	printCityData(cityData)

	fullName = cityData["name"]
	locationInfo = fullName.split(",")
	cityName = locationInfo[0]
	stateName = locationInfo[1][1:]

	return {"cityName": cityName, "stateName": stateName}




def checkWeather():
	apiData = API_Data()

	curURL = urllib.urlopen(apiData.fullURL)
	rawData = [line[:-1] for line in curURL.readlines()]
	weatherRawJSON = "".join(rawData)

	weatherJSON = json.loads(weatherRawJSON)

	curWeather = weatherJSON["current_observation"]

	# curLocation = Location(curWeather["display_location"], "display_location")
	# observationLocation = Location(curWeather["observation_location"], "observation_location")
	weatherMetrics = WeatherMetrics(curWeather)
	# summary = WeatherSummary(weatherMetrics)
	summary = u"The weather in {} is {}.  The temperature is currently {}".format(weatherMetrics.curLocation.city, weatherMetrics.weather, weatherMetrics.temperature_string)

	# respond(weatherMetrics.weather)
	respond(summary)


	

# apiKey = None
# myPath = os.path.dirname(os.path.realpath(__file__))
# subdir = "weatherUnderground"
# newPath = "/".join([myPath, subdir, "apiData.json"])
# rawData = None
# jsonData = None

# with open(newPath, "r") as myFile:
# 	rawData = myFile.readlines()
# 	jsonData = json.loads(" ".join(rawData))

# pretext = jsonData["pretext"]
# posttext = jsonData["posttext"]
# apiKey = jsonData["apiKey"]
# town = "{}.json".format(jsonData["hometown"])
# state = jsonData["homestate"]
# searchPrefix = jsonData["search_prefix"]
# fullURL = "/".join([pretext, apiKey, posttext, state, town])
def test():
	apiData = API_Data()

	curURL = urllib.urlopen(apiData.fullURL)
	rawData = [line[:-1] for line in curURL.readlines()]
	weatherRawJSON = "".join(rawData)

	weatherJSON = json.loads(weatherRawJSON)

	curWeather = weatherJSON["current_observation"]

	# curLocation = Location(curWeather["display_location"], "display_location")
	# observationLocation = Location(curWeather["observation_location"], "observation_location")
	weatherMetrics = WeatherMetrics(curWeather)

	printSummary(weatherMetrics)

	cityName = raw_input("Enter city name to search: ")
	searchResults = searchCity(cityName)
	print "|{}|".format(searchResults["cityName"])
	print "|{}|".format(searchResults["stateName"])

# newURL = "/".join([apiData.pretext, apiData.apiKey, apiData.posttext, state, cityName])

# newMetrics = getMetrics()