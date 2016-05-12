#!/usr/bin/env python

import sys
import os
import json
import wolframalpha
import wap
import urllib2
import greetings
from mainhome import home
from respond import respond
import random


user = "Chris"

gratefulTerms = ["thanks", "thank you", "i appreciate"]
welcomeResponses = ["You're very welcome, sir.", "My pleasure.", "Of course.", "No problem."]

print ""

greetings.welcome(user)

response = ''
question = ''
last_response = ""
skip = False
iteration = 1


while "done" not in question:
	if iteration > 1:
		respond("Is there anything else I can help you with?")
	else:
		respond("What can I do for you?")
	activity = raw_input("\n ")
	print ""
	activity = activity.lower()
	# print activity
	for term in gratefulTerms:
		if term in activity:
			x = random.randint(0,len(welcomeResponses)-1)
			# print "x =",x
			# respond(welcomeResponses[x])
			skip = True
			break

	if activity == last_response and skip == False:
		respond("I just told you...")

	home(activity)
	last_response = activity
	iteration += 1