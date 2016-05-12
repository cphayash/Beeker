#!/usr/bin/env python

import pyttsx
import re


def respond(string):
	degrees = u"\u00b0"

	engine = pyttsx.init()
	#engine.setProperty('voice', 'com.apple.speech.synthesis.voice.serena.premium')
	# if last_response == string:
	# 	engine.say("I just told you... ")
	speech = re.sub("\|","...",string)
	speech = re.sub("\n","...",speech)
	str_response = speech
	speech = re.sub(degrees + "F", degrees + "Farenhite",speech)
	speech = re.sub(degrees + "C", degrees + "Celcius",speech)
	engine.say(speech)
	print str_response
	#print string + "\n"
	#print "About to runAndWait()"
	engine.runAndWait()
	#print "made it past runAndWait()"
	#engine.stop()
	#print "made it past stop()"
	# last_response = string
