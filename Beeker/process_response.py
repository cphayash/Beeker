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
from getTime import getTime
import aboutMe
from mapIt import googleMaps
# from weatherCheck import getWeather, getForecast
import weatherCheck
import re
import wikipedia
import searchWiki
from findSpaceStation import locateISS
import random
import string
from weatherUnderground import checkWeather


def stripPunc(phrase, punctuation, saveMarks):
	for mark in punctuation:
		if str(mark) not in saveMarks:
			phrase = phrase.replace(mark, "")
	# return ''.join(char for char in phrase_list if char not in punctuation)
	return phrase

def process(activity):
	# print activity
	# activity_list = activity.split()
	punctuation = set(string.punctuation)
	plainTerms = ["a", "e", "i", "o", "u", "y", "me", "you", "of", "in", "for", "at", "the", "an"]
	locSearchTerms = ["find", "locate", "located", "location", "where", "search for"]
	ISSterms = ["international space station", "the space station", "space station", "iss"]
	googleMapsTerms = ["map", "maps", "google"]
	aboutMeQuestions = ["who are you?", "who are you", "what is your name?", "what is your name", "explain yourself", "tell me about yourself"]
	doneTerms = ["quit", "done", "nevermind", "leave", "leave me alone", "shutdown", "no"]
	doneMatchTerms = ["quit", "done", "leave", "peace", "bye", "goodbye", "shutdown", "shut down", "turn off", "off"]
	gratefulTerms = ["thanks", "thank you", "i appreciate", "please"]
	shutdownTerms = ["shutdown", "shut down", "off", "turn off"]
	welcomeResponses = ["You're very welcome, sir.", "My pleasure.", "Of course."]
	doneTerms = doneTerms + doneMatchTerms + shutdownTerms
	activityClean = stripPunc(activity, punctuation, [])
	activityPosNeg = stripPunc(activity, punctuation, ["+", "-"])
	activity_list = activityClean.split()
	activity_list_pos_neg = activityPosNeg.split()
	# print activity_list_pos_neg


	if activity[:len("mdfind")].lower() == "mdfind":
		# print os.system(activity)
		search_results = str(os.system(activity))
		# print search_results
		# print type(search_results)
		line_count = 0
		# while line_count < 5:
		# 	print search_results[line_count]
		# 	line_count += 1
		return True

	"""The following for loop checks if gratefulTerms[x] in IN the activity string, or if it IS the activity string.  
	Once it finds a match, either it leaves the function, or it leaves the for loop and continues throught the function"""
	for term in gratefulTerms:
		if term in activity:
			x = random.randrange(0,len(welcomeResponses))
			respond(welcomeResponses[x])
			if term == activity:
				return True
			else:
				break


	for term in aboutMeQuestions:
		if activity == term:
			aboutMe.iAmBeeker()
			return True
	if activity[:len('wiki')] == "wiki" or activity[:len('wikipedia')] == "wikipedia":
		# respond(wikipedia.summary(activity[len('wiki'):]))
		searchWiki.getWiki(activity)
		return True
	if activity[:len('summarize')] == "summarize" or activity[:len('summary')] == "summary":
		# respond(wikipedia.summary(activity[len('summarize'):], sentences = 2))
		searchWiki.getWiki(activity)
		return True
	if 'question' in activity:
		respond("What would you like to know?")
		question = raw_input("\n ")
		question = question.lower()

		print '\n'
	
		if question == 'quit()' or 'done' in question or 'nevermind' in question:
			greetings.anyMoreQuestions()
		else:
			ask(question)
			return True
	if 'time' in activity and 'in' not in activity:
		if getTime(activity) == False:
			respond("That didn't make sense")
		return True
	if "weather" in activity or "forecast" in activity:
		# pattern = re.compile("\\b(of|the|in|for|at|weather|check|find|how|how's|is|tell|me|check|out|about)\\W", re.I)
		# string = re.sub(pattern, "", activity)
		# string = string.replace(" ", "")
		if "forecast" in activity:
			weatherCheck.getForecast(activity)
		else:
			# weatherCheck.getWeather(activity)
			checkWeather()
		respond("Finished weather check")
		return True


	
	for term in ISSterms:
		if term in activity.lower():
			# print "Found:", term
			for word in locSearchTerms:
				if word in activity:
					# print "Found:", word
					locateISS()
					return True

	# for term in acivity:
	# 	term = term.lower()
		# if term in locSearchTerms and term in ISSterms:
		# 	locateISS()
		# elif term in locSearchTerms and term in googleMapsTerms:
	for term in googleMapsTerms:
		if term in activity_list_pos_neg:
			try:
				latitude = float(activity_list_pos_neg[1])
				longitude = float(activity_list_pos_neg[2])
				# print latitude, longitude
				googleMaps(latitude, longitude, True)
			except:
				respond("If you're trying to use Google Maps, make sure to use two numbers")
			return True



	grateful = False

	for term in doneTerms:
		if term in activity:
			# print "Found a doneTerms item:",activity
			if 'off' in activity or 'down' in activity or 'shut' in activity:
				for item in shutdownTerms:
					if item == activity:
						greetings.shutdownGoodbye()
						sys.exit(0)
				if 'piss off' in activity or 'fuck off' in activity:
					greetings.madGoodbye()
					sys.exit(0)
		if activity[len(activity)-len(term):] == term or activity[:len(term)] == term:
			# print "Found a doneTerms item at end of string:", activity
			for term in gratefulTerms:
				if term in activity:
					grateful = True
			if grateful == False:
				respond("Very well, sir.")		
			greetings.goodbye()
			sys.exit(0)
		
	return False