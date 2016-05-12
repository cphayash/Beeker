#!/usr/bin/env python

import datetime
import time
import pyttsx
from respond import respond
from getTime import currentTime

def welcome(user):
	engine = pyttsx.init()
	current_hour = time.localtime().tm_hour
	current_time = "{0}:{1}:{2}".format(str(time.localtime().tm_hour).zfill(2),str(time.localtime().tm_min).zfill(2),str(time.localtime().tm_sec).zfill(2))

	if current_hour < 12:
		respond("Good morning, " + user + "!")
	elif current_hour > 12 and current_hour < 18:
		respond("Good afternoon, " + user + "!")
	elif current_hour >= 18 and current_hour <=23:
		respond("Good evening, " + user + "!")
	else:
		respond("Hello, " + user + "!")
	# print "Made it out of the conditional!"
	respond("The current time is " + currentTime())


def goodbye():
	respond("Start me up again if there is anything else you need! Goodbye!")


def madGoodbye():
	respond("Well that's quite an dirty mouth you have!  Let me know if you need anything else once you check your attitude.  Good day!")


def shutdownGoodbye():
	respond("Shutting down...  Goodbye!")

def anyMoreQuestions():
	respond("Alright.  Let me know if there are any other questions you'd like me to answer for you")