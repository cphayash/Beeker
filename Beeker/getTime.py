#!/usr/bin/env python

import sys
import os
import json
import wolframalpha
import wap
import urllib2
import greetings
from respond import respond
from ask import ask
import time

def getTime(activity):
	timeTerms = ['tell me', 'what is', 'current', 'what time is it']
	for term in timeTerms:
		if term in activity:
			respond("The time is " + currentTime())
			return True
	return False

def currentTime():
	return time.strftime("%I:%M %p")