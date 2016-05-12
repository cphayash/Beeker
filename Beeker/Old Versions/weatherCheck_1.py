#!usr/bin/env python

import sys
import os
# import json
import wolframalpha
import wap
import urllib2
import greetings
from respond import respond
from ask import ask
from getTime import getTime
import aboutMe
import requests
from pprint import pprint
from tempConvert import kelToFar
import re

class WeatherObject(object):
	def __init__(self):
		self.temp = ""
		self.temp_max = ""
		self.temp_min = ""
		self.pressure = ""
		self.humidity = ""

def getWeather(activity):
	pattern = re.compile("\\b(of|the|in|for|at|weather|check|find|how|how\'s|is|tell|me|check|out|about)\\W", re.I)
	string = re.sub(pattern, "", activity)
	place = string.replace(" ", "")

	url = "http://api.openweathermap.org/data/2.5/weather?q="+place

	new_stuff = requests.get(url)

	weather = WeatherObject()
	pprint(new_stuff.json())

	print "---------------------------------"

	for item,part in new_stuff.json().iteritems():
		# print item
		if item == "name":
			weather.name = str(part)
		if item == "main":
			# print part,type(part)
			weather.temp = str(kelToFar(float(part["temp"])))
			weather.temp_max = str(kelToFar(part["temp_max"]))
			weather.temp_min = str(kelToFar(part["temp_min"]))
			weather.pressure = str(part["pressure"])
			weather.humidity = str(part["humidity"])
			# respond("The current temperature is " + str(kelToFar(float(part["temp"]))) + " degrees Farenheit")
			# respond("The high for today is estimated at " + str(kelToFar(part["temp_max"])) + " and the low for today is estimated at " + str(kelToFar(part["temp_min"])))
			# respond("The barometric pressure is currently " + str(part["pressure"]) + " mbar, and the humidity is " + str(part["humidity"]) + "%")
			# respond("")
		if item == "weather":
			weather.description = str(part[0]["description"]).lower()
			# detail = str(part[0]["description"])
			# if "sky" in detail or "Sky" in detail:
			# 	respond("The " + detail + " today.")
			# else:
			# 	respond("Walk outside today and you'll see " + detail)
		# else:
		# 	pass
	if weather.name in activity:
		print "weather.name:", weather.name
		print "activity:", activity
		if "sky" in weather.description:
			print "I got into the weather.name in activity statement"
			respond("The " + weather.description + " in " + weather.name + " today.")
		else:
			respond("Walk outside in " + weather.name + " today and you'll see " + weather.description)
	else:
		print "I'm in the else statement"
		if "sky" in weather.description:
			respond("The " + weather.description + " today.")
		else:
			respond("Walk outside today and you'll see " + weather.description)
	respond("The current temperature there is " + weather.temp + " degrees Farenheit")
	respond("The high for today is estimated at " + weather.temp_max + " and the low is estimated at " + weather.temp_min)
	respond("The barometric pressure is currently " + weather.pressure + " mbar, and the humidity is " + weather.humidity + "%")