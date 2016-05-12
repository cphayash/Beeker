#!/usr/bin/env python

import sys
import os
import json
import wolframalpha
import wap
import urllib2
import greetings
from respond import respond
import wikipedia
import searchWiki

def ask(question):
	client = wolframalpha.Client('4RGXHJ-J875THLRR9')
	try:
		response = client.query(question)

		try:
			# print(next(response.results).text)
			respond(next(response.results).text)
		except Exception, e:
			try:
				searchWiki.getWiki(question)
			except Exception, e:
				respond("I'm really sorry.  I'm having a hard time finding results for this.")
				# print('Oh, fuck... I goofed... {0}'.format(e))
				print e


	except Exception, e:
		if "not known" in str(e):
			respond("There seems to be an issue with your internet connection.")
		else:
			respond("I encountered an unknown error.  My apologies.")
			print e
	print "\n"

	

	print '\n'


	# The issue is the way the variable "string" is being processed.  Look into the re.sub function...